import misc_tools
import random
from pseudo_DB import dbCall

def create_routing(env, first_step='move5'):


## if you have a problem with one of the values,
## just update outside of the tasks dictionary for now
    tasks = {
    
        'move5': {
            'location': env['forklift'], #previously 'OPTX_storage'
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 1,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op5'
        },

        'op5': misc_tools.make_quality_step(
            env=env,
            run_time=dbCall("SIP_insp"),
            route_to='op7',
            transit_time=0
            ),

        'op7': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0,
            'run_time': dbCall("OPTX_assy"),
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op8'
        },

        'op8': {
        # is this even the right location and worker combination? Check!
            'location': env['assembly_bench'],
            'worker': env['technician'],
            # this step is an unmanned step --> update appropriately!!
            'manned': False,
            'setup_time': 0,
            'run_time': 1, # assuming always 1 because this is automated inspection
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op9'
        },

        'op9': {
            'location': env['OPTX_CTI'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 5,
            'run_time': dbCall("OPTX_CTI"),
            'teardown_time': 1,
            'transit_time': 0,
            'route_to': env['OPTX_kanban']
        }
    }
    return misc_tools.make_steps(first_step=first_step, tasks=tasks)

#need to update the below steps, but see if it fixes the error
    #tasks['op5']['setup_time'] = 1
    #tasks['op5']['teardown_time']=1


def create_kanban_attrs(env):

    return misc_tools.make_kanban_attrs(order_gen=env['gener.OPTX'],
                                        order_point=20, order_qty=50,
                                        init_qty=50, warmup_time=0)
    # what are the details of this specific kanban?order point, order quantity, etc.
    # because I just made mine up


    