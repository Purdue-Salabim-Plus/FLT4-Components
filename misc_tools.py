import salabim as sim
import copy
import random

def make_shifts(shift_duration, off_days=[]):
        
    shifts = []
    week = [
        'monday','tuesday','wednesday','thursday',
        'friday','saturday','sunday'
    ]

    for day in week:
        tmp = {}
        tmp['day'] = day

        if day in off_days:
            tmp['shift_duration'] = 0
            tmp['off_duration'] = 1440

        else:
            tmp['shift_duration'] = shift_duration
            tmp['off_duration'] = 1440 - shift_duration
            
        shifts.append(tmp)
        
    return shifts

def make_steps(first_step, tasks):
    """
    """
    
    step = first_step 
    fail_count = 0
    steps = []
    while True:
        # details = copy.deepcopy(tasks[step])
        details = tasks[step]

        if 'yield' in details.keys(): # if the yield of this step is less than 100% --> if some will be sent to rework
            if random.random() < details['yield']: #generates a random number 0 - 1, checks if less than the yield value
                details['result'] = 'pass'
                details['route_to'] = details['route_to_pass']
            else:
                details['result'] = 'fail'
                details['route_to'] = details['route_to_fail']
        elif 'fail_count' in details.keys():
            fail_count += 1
            if fail_count == details['fail_count']:
                details['route_to'] = details['route_to_pass']
            else:
                details['route_to'] = details['route_to_fail']

        steps.append(details)
        
        if isinstance(details['route_to'], str):
            step = copy.deepcopy(details['route_to'])
        else:
            break
        
    return steps

def make_assembly_step(env, run_time, route_to, manned=True, transit_time=0):
    """
    """

    return {
        'location': env['assembly_bench'],
        'worker': env['assembler'],
        'manned': manned,
        'setup_time': 0,
        'run_time': run_time,
        'teardown_time': 0,
        'transit_time': transit_time,
        'route_to': route_to
    }

def make_kanban_attrs(order_gen, order_point, order_qty, init_qty, 
                      warmup_time):
    """
    """

    return {
        'order_gen': order_gen,
        'order_point': order_point,
        'order_qty': order_qty,
        'init_qty': init_qty,
        'warmup_time': warmup_time
    }

# def make_unmanned_test_step(location, run_time, yield_rate, ):
#     """
#     """

#     return {
#         'location': plps_bench,
#         'worker': test_tech,
#         'manned': True,
#         'setup_time': 1, # broken up until batching in place (15/100)
#         'run_time': sim.Uniform(5, 10),
#         'teardown_time': 0, # broken up until batching in place (30/100), baked in with setup
#         'transit_time': 1,
#         'yield': 0.99,
#         'route_to_pass': 'op3',
#         'route_to_fail': scrap
#     }

# def make_manned_test_step():
    # """
    # """

def make_quality_step(env, run_time, route_to, transit_time=0, **kwargs):
    """
    """

    return {
        'location': env['quality_bench'],
        'worker': env['qual_inspector'],
        'manned': True,
        'setup_time': 0,
        'run_time': run_time,
        'teardown_time': 0,
        'transit_time': transit_time,
        'route_to': route_to
    }

def calc_current_pass_yield(env, run_time, initial_FPY, final_FPY, **kwargs):
    """
    Calculates the pass yield for machines that are not a static pass yield rate
    Currently evenly scales over time (based on active time) 
    but includes nights and weekends, assuming one shift of 8 hours a day
    Assume that run_time is the time that the machines will improve over (in minutes)
    initial_FPY is the first pass yield at the beginning of the run time
    final_FPY is the first pass yield at the end of the run time

    ** could I send in the current 'current_pass_yield' and then check if the machines are active? 
    BUT, will there even be requests for the pass yield if the machines are down for the night?
    """
    OTN = env.now()/3 #calculates operational time of the machines up until now
    scale_factor = (initial_FPY - final_FPY)/(run_time/3) #dividing by 3 gets the operational time of machines, assuming 1 8-hour shift
    current_pass_yield = initial_FPY + OTN*scale_factor
    return current_pass_yield




