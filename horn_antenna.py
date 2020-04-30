import misc_tools
import random

INIT_QT = 1000


def create_routing(env, first_step='move18'):

	tasks={
		# I added this move step in to create a place for the horn antenna to arrive
		# but do we need to take out to stay true to the Excel doc?
		'move18': {
            'location': env['forklift'],
            # is this the right location to have the move take place from?
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': .1,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op18'
        },

		'op18': {
			'location': env['assembly_bench'],
			'worker': env['assembler'],
			'manned': True,
			'setup_time': 0.66,
			'run_time': 3.61,
			'teardown_time': 0.61,
			'transit_time': 0,
			'route_to': 'op19'
		},

		'op19':  misc_tools.make_quality_step(
			env=env,
			run_time=0.2,
			route_to='op20',
			transit_time=0,
			),

		'op20': {
			'location': env['MOD_FEEDASSY_PAT'],
			'worker': env['technician'],
			'manned': True,
			'setup_time': 0.5,
			'run_time': 0.5,
			'teardown_time': 0.5,
			'transit_time': 0,
			'yield': 0.9423,
			'route_to_fail': 'op20_debug',
			'route_to_pass': env['horn_antenna_kanban']
		},

		'op20_debug': {
			'location': env['MOD_FEEDASSY_PAT'],
			'worker': env['technician'],
			'manned': True,
			'setup_time': 0,
			'run_time': random.uniform(a=60,b=200),
			'teardown_time': 0,
			'transit_time': 0,
			'route_to': env['horn_antenna_kanban']
		}
		
	}
	return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def create_kanban_attrs(env):

	return misc_tools.make_kanban_attrs(order_gen=env['gener.horn_antenna'],
		order_point=2, order_qty=5,
		init_qty=INIT_QT, warmup_time=0)

#ORIG : 5
