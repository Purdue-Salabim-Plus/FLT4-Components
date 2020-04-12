import misc_tools
import random

def create_routing(env, first_step='move1'):

	tasks={
		'move1': {
			'location': env['forklift'], 
			'worker': env['production_control'],
			'manned': False,
			'setup_time': 0,
			'run_time': 0,
			'teardown_time': 0,
			'transit_time': 0,
			'route_to': env['cover_kanban']
		}
	}


	return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def create_kanban_attrs(env):

	return misc_tools.make_kanban_attrs(order_gen=env['gener.cover'],
		order_point=20, order_qty=50,
		init_qty=50, warmup_time=0)
	# what are the details of this specific kanban?order point, order quantity, etc.
	# because I just made mine up
	
