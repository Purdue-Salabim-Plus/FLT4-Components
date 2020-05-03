import numpy

def time_curve(initial_FPY, final_FPY, final_time):

	### Learning curve by time alone
	### initial_FPY is the pass yield at the beginning of the time epoch
	### final FPY is the pass yield at the end of the time epoch
	### final_time is the amount of time that the machine increases from initial to final FPY during
	### based on equation y(t) = c/(1+a*e^(-bt))
	### b must be >0
	### c is the end value of the FPY in percentage (so a complete
	### FPY would be 100)
	### c/(1+a) is the initial value of the FPY in percentage

	c = final_FPY
	print(c)
	#Know that y(0) = c / (1+a), so calculate a
	a = c/initial_FPY - 1 
	print(a)
	#Also know that y(final_time) = c, so calculate b from this
	mid_1 = ((c/(c-.1))-1)/a #need to subtract .1 from c so we don't end up with 0
	mid_2 = numpy.log(mid_1)
	b = -mid_2/final_time

	time_arguments = [a,b,c]

	return time_arguments


def time_yield_calc(env, a, b, c):

	current_time = env.now()
	current_pass_yield = c/(1+a*numpy.exp(-b*current_time))

	return current_pass_yield


def jobs_processed_curve(initial_FPY, final_FPY, final_units):

	### Learning curve by the number of jobs processed
	### initial_FPY is the pass yield at the beginning of the time epoch
	### final FPY is the pass yield at the end of the time epoch
	### final_units is the number of jobs that the machine needs to process to be at the final FPY
	### based on equation c_N = c_1*N^(alpha), where alpha = log(learning curve decimal)/log(2)
	### note: for this, all rates need to be in decimals

	mid_1 = final_FPY/initial_FPY
	alpha = numpy.log(mid_1)/numpy.log(final_units)
	K = numpy.power(10,(alpha*numpy.log10(2)))

	return K


def jobs_yield_calc(env, initial_FPY, K, jobs_processed):

### for this to work, we would also have to track the number of jobs that
### have been processed on a given machine. So, in class Machine, you could
### add a self.jobs_processed = 0 argument in the def __init__ section.
### in the def process_entity(self), you could add self.jobs_processed = 
### self.jobs_processed + 1. Then, you would send MachineName.jobs_processed
### into this function

	current_pass_yield = initial_FPY*numpy.power(jobs_processed,numpy.log10(K)/numpy.log10(2))
	return current_pass_yield




