import misc_tools
import random
from pseudo_DB import dbCall

# this is taking section_C and the cover and merging into one set of parts

def create_routing(env, first_step='op29'):

    tasks = {
        'op29': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.09,
            'run_time': dbCall("Top_cover_install"),
            'teardown_time': 0.1,
            'route_to': 'op30'
        },

        'op30': {
            'location': env['static_CTI'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 0.77,
            'run_time': dbCall("Confidence_test_final"),
            'teardown_time': 0.77,
            'transit_time': 0,
            'yield': 94.23,
            'route_to_pass': 'op30a',
            'route_to_fail': 'op31'
        },

        'op31': {
            'location': env['static_CTI_DBG'],
            'worker': env['technician'],
            'manned': True,
            'setup_time':0,
            'run_time': 60,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op30'

        },

# op30a is just a buffer step to split the jobs that need more processing from the ones that don't
# there is DEFINITELY a better way to do this, I just don't know what it is yet
        'op30a': {
            'location': env['static_CTI'],
            'worker': env['technician'],
            'manned': False,
            'setup_time': 0,
            'run_time': 0,
            'teardown_time': 0,
            'transit_time': 0,
            'yield': 90,
            'route_to_pass': 'op33',
            'route_to_fail': 'move32'
        },

        'move32': {
            'location': env['static_CTI'],
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 1,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op32'
        },

        'op32': {
            'location': env['COND_EST'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 0.5,
            'run_time': dbCall("Thermal_test"),
            'teardown_time': 0.5,
            'route_to': 'move33'
        },

        'move33': {
            'location': env['COND_EST'],
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 0.0084,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op33'

        },

        'op33': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.09,
            'run_time': dbCall("Top_cover_seal"),
            'teardown_time': 0.07,
            'route_to': env['section_D_kanban']
        }

    }

    return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def get_bom(env):
    # note that these quantities are not double checked, so they are 
    # just placeholders for now

    return {
        'section_C': {
            'location': env['section_C_kanban'],
            'qty': 1
        },
        'cover': {
            'location': env['cover_storage'],
            'qty': 1
        }
    }

def create_kanban_attrs(env):

    return misc_tools.make_kanban_attrs(order_gen=env['gener.section_D'],
        order_point=0, order_qty=0,
        init_qty=0, warmup_time=0)
    # what are the details of this specific kanban?order point, order quantity, etc.
    # because I just made mine up
    

	