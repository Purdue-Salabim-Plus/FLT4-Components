import misc_tools
import random


INIT_QT = 100


def create_routing(env, first_step='op26'):
    

    tasks = {

    # Does the first step here need to be a move step to approximate the different pieces coming together?
        'op26': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.3,
            'run_time': 2.81,
            'transit_time': 0,
            'teardown_time': 0.16,
            'route_to': 'op27'
        },
        'op27': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.14,
            'run_time': 1.91,
            'transit_time': 0,
            'teardown_time': 0,
            'route_to': 'op28'
        },

        'op28': {
            'location': env['quality_bench'],
            'worker': env['qual_inspector'],
            'manned': True,
            'setup_time': 0,
            'run_time': 75,
            'transit_time': 0,
            'teardown_time': 0,
            'route_to': env['section_C_kanban']
            #'route_to': env['section_C_storage']
        }

    }

    return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def get_bom(env):
    # note that these quantities are not double checked, so they are 
    # just placeholders for now

    return {
        'section_B': {
            'location': env['section_B_kanban'],
            'qty': 1
        },
        'antenna_kit': {
            'location': env['antenna_kit_kanban'],
            'qty': 1
        }

    }

def create_kanban_attrs(env):

    return misc_tools.make_kanban_attrs(order_gen=env['gener.section_C'],
        order_point=10, order_qty=10,
        init_qty=INIT_QT, warmup_time=5)
    #Originally init_qty = 20

    