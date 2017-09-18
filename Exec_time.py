"""
							EXECUTION TIME
	This module is used to get the total execution time when this ran 
	sucessfully

	NOTE:The below start , stop , execution_time must be in the main file which
		 will be executed.
"""
# == Imports ===================================================================

import timeit
import time 

# == Main Arguments ============================================================

start = timeit.default_timer()

# Statements that need to executed
time.sleep(5)# to Stimulate Execution of 5 sec

stop = timeit.default_timer()

execution_time = stop - start
#Execution Time is returned in "Sec"
print(execution_time)

# == END =======================================================================