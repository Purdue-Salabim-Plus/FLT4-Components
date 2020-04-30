import misc_tools
import random

INIT_QT = 1000

def create_routing(env, first_step='move1'):

    tasks={
        'move1': {
            'location': env['forklift'], #was env['multiplexer_storage']
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 0.012,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op1'
        },
        
        'op1': misc_tools.make_assembly_step(
            env=env,
            run_time = 3.79,
            route_to='op2'
            ),

        'op2': misc_tools.make_quality_step(
            env=env,
            run_time=0.2,
            route_to='op3',
            transit_time=0
            ),

        'op3': {
            'location': env['VSWR_CTI'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 0.09,
            'run_time': 1.24,
            'teardown_time': 0.07,
            'transit_time': 0,
            'yield': 0.99,
            'route_to_pass': env['multiplexer_kanban'],
            'route_to_fail': 'op4'
        },

        'op4': {
            'location': env['VSWR_CTI_DBG'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 0.5,
            'run_time': random.uniform(a=60,b=120),
            'teardown_time': 0.5,
            'transit_time': 0,
            'route_to': env['multiplexer_kanban']
        }
    }
    tasks['op1']['teardown_time'] = 0.14
    tasks['op1']['setup_time'] = 0.21

    return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def create_kanban_attrs(env):

    return misc_tools.make_kanban_attrs(order_gen=env['gener.multiplexer'],
        order_point=20, order_qty=50,
        init_qty=INIT_QT, warmup_time=0)

    # Originally: 50

    # what are the details of this specific kanban?order point, order quantity, etc.
    # because I just made mine up
    
