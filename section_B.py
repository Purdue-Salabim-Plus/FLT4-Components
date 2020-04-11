import misc_tools
import random

# this is taking section_A and the bfpd and the splitter and merging them into one group of items

def create_routing(env, first_step='move23'):

    tasks = {
        'move23': {
            'location': env['forklift'], #formerly section_A_kanban
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 1,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op23'
        },
        'op23': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.04,
            'run_time': 0.64,
            'transit_time': 0,
            'teardown_time': 0.03,
            'route_to': 'op24'
        },
        'op24': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.16,
            'run_time': 1.65,
            'teardown_time': 0.12,
            'transit_time': 0,
            'route_to': 'op25'
        },
        
        'op25': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.04,
            'run_time': 0.58,
            'transit_time': 0,
            'teardown_time': 0.03,
            'route_to': env['section_B_kanban']
            #'route_to': env['section_B_storage']
        }

    }

    return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def get_bom(env):
    # note that these quantities are not double checked, so they are 
    # just placeholders for now

    return {
        'section_A': {
            'location': env['section_A_kanban'],
            'qty': 1
        },
        'BFPD': {
        # ensure that the other folks called these bfpd and splitter
            'location': env['BFPD_kanban'],
            'qty': 1
        },
        'splitter': {
            'location': env['splitter_kanban'],
            'qty': 1
        }
    }

def create_kanban_attrs(env):

    return misc_tools.make_kanban_attrs(order_gen=env['gener.section_B'],
        order_point=10, order_qty=10,
        init_qty=20, warmup_time=5)
    # what are the details of this specific kanban?order point, order quantity, etc.
    # because I just made mine up
    

	