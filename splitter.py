import misc_tools
import random

INIT_QT = 1000



def create_routing(env, first_step='move15'):
    tasks = {

        'move15': {
            'location': env['forklift'], #formerly splitter storage
            # is this the right location to have the move take place from?
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 1,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op15'
        },

        'op15': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 1,
            'run_time': 5,
            'teardown_time': 1,
            'transit_time': 1,
            'route_to': 'move16'
        },

        'move16': {
            'location': env['assembly_bench'],
            # is this the right location to have the move take place from?
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 1,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op16'
        },

        'op16': misc_tools.make_quality_step(
            env=env,
            run_time=2,
            route_to='move17',
            transit_time=1
        ),

        'move17': {
            'location': env['quality_bench'],
            # is this the right location to have the move take place from?
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 1,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op17'
        },

        'op17': {
            'location': env['VSWR_CTI'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 10,
            'run_time': 2,
            'teardown_time': 10,
            'transit_time': 1,
            'yield': 94.23,
            'route_to_pass': env['splitter_kanban'],
            'route_to_fail': 'op17_debug'
        },

        'op17_debug': {
            'location': env['VSWR_CTI'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 0,
            'run_time': random.uniform(a=60,b=200),
            'teardown_time': 0,
            'transit_time': 0,
            'route_to_': env['splitter_kanban'],
        },

    }

    return misc_tools.make_steps(first_step=first_step, tasks=tasks)


def create_kanban_attrs(env):
    return misc_tools.make_kanban_attrs(order_gen=env['gener.splitter'],
                                        order_point=2, order_qty=5,
                                        init_qty=INIT_QT, warmup_time=0)



#init qty: 5