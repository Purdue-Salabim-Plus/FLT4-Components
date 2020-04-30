import misc_tools
import random

INIT_QT = 1000


def create_routing(env, first_step='move10'):


## if you have a problem with one of the values,
## just update outside of the tasks dictionary for now
	tasks = {

		'move10': {
			'location': env['forklift'], #formerly BFPD_storage
			'worker': env['production_control'],
			'manned': True,
			'setup_time': 0,
			'run_time': 1,
			'teardown_time': 0,
			'transit_time': 0,
			'route_to': 'op10'
		},
		
		'op10': {
			'location': env['assembly_bench'],
			'worker': env['assembler'],
			'manned': True,
			'setup_time': 5,
			'run_time': 10,
			'teardown_time': 5,
			'transit_time': 0,
			'route_to': 'move11'
		},

		'move11': {
			'location': env['assembly_bench'], #how do we make sure this is the same assembly bench
											   #that the last operation left off from?
			'worker': env['production_control'],
			'manned': True,
			'setup_time': 0,
			'run_time': 1,
			'teardown_time': 0,
			'transit_time': 0,
			'route_to': 'op11'
		},

		'op11': {
		# is this appropriate? Because the excel doc doesn't have information on who does the step
			'location': env['assembly_bench'],
			'worker': env['assembler'],
			'manned': False,
			'setup_time': 1,
			'run_time': 5,
			'teardown_time': 1,
			'transit_time': 0,
			'route_to': 'move13'
		},

		'move13': {
			'location': env['assembly_bench'], #how do we make sure this is the same assembly bench
											   #that the last operation left off from?
			'worker': env['production_control'],
			'manned': True,
			'setup_time': 0,
			'run_time': 1,
			'teardown_time': 0,
			'transit_time': 0,
			'route_to': 'op13'
		},

		'op13': {
			'location': env['BFPD_CTI'],
			'worker': env['technician'],
			'manned': True,
			'setup_time': .5,
			'run_time': 4,
			'teardown_time': .5,
			'transit_time': 0,
			'yield': .9423,
			'route_to_pass': env['BFPD_kanban'],
			'route_to_fail': 'move14'
		},

		'move14': {
			'location': env['BFPD_CTI'], 
			'worker': env['production_control'],
			'manned': True,
			'setup_time': 0,
			'run_time': 1,
			'teardown_time': 0,
			'transit_time': 0,
			'route_to': 'op14'
		},

		'op14': {
		# check back to excel doc: this doesn't exactly agree with the number provided.
		# do we need to add another rework within operation 14??
		# also, op14 is not in the diagram, what are the implications of that?
			'location': env['BFPD_CTI_DBG'],
			'worker': env['technician'],
			'manned': True,
			'setup_time': 0.5,
			'run_time': random.uniform(a=60,b=200),
			'teardown_time': 0.5,
			'transit_time': 0,
			'route_to': env['BFPD_kanban']
		}
		
	}

	return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def create_kanban_attrs(env):

	return misc_tools.make_kanban_attrs(order_gen=env['gener.BFPD'],
										order_point=20, order_qty=50,
										init_qty=INIT_QT, warmup_time=0)

# INITQTY = 50
	# what are the details of this specific kanban?order point, order quantity, etc.
	# because I just made mine up


	