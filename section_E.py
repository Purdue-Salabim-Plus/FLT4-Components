import misc_tools
import random
from pseudo_DB import dbCall

# this is taking section_C and the cover and merging into one set of parts

def create_routing(env, first_step='move34'):

    tasks = {
        'move34': {
            'location': env['section_D_kanban'],
            # is this the right location to have the move take place from?
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 0.06,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op34'
        },

        'op34': {
            'location': env['assembly_bench'],
            # make sure that this assembly bench is the same place that the next move picks up from!!
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.05,
            'run_time': dbCall("Antenna_install"),
            'teardown_time': 0.05,
            'route_to': 'op35'
        },

        'op35': {
            'location': env['RF_Fit_Test'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 0.26,
            'run_time': dbCall("RF_fit_test"),
            'teardown_time': 0.16,
            'transit_time': 0,
            'yield': 94.23,
            'route_to_pass': 'move36',
            'route_to_fail': 'op35_debug'
        },

        'op35_debug': {
            'location': env['RF_Fit_Test'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 0,
            'run_time': 30,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to_': 'move36',
        },

        'move36': {
            'location': env['RF_Fit_Test'],
            # is this the right location to have the move take place from?
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 1,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op36'
        },

        ## op36 is supposed to have a batch size of 8: how do you accommodate that?
        ## build it out into its own special step and have a bom for it?
        'op36': {
            'location': env['RF_CFG'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 2,
            'run_time': dbCall("RF_test"),
            'teardown_time': 2,
            'route_to': 'op37'
        },

        'op37': misc_tools.make_quality_step(
            env=env,
            run_time=dbCall("Inspection_final"),
            route_to=env['FLT4_storage'],
            transit_time=0
            )
    }

    return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def get_bom(env):
    # note that these quantities are not double checked, so they are 
    # just placeholders for now

    return {
        'section_D': {
            'location': env['section_D_kanban'],
            'qty': 1
        },
        'horn_antenna': {
            'location': env['horn_antenna_kanban'],
            'qty': 1
        }
    }

# def create_kanban_attrs(env):

#     return misc_tools.make_kanban_attrs(order_gen=env['gener.section_D'],
#         order_point=0, order_qty=0,
#         init_qty=0, warmup_time=0)
    # what are the details of this specific kanban?order point, order quantity, etc.
    # because I just made mine up
    

	