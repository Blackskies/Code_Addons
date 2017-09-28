"""
				CONVERTING EPOCH TIME TO GENERAL READABLE TIME MODULE
"""
# == Imports ===================================================================
import datetime
# == Input Time ================================================================

def epoch2time(time):
	"""
	This converts epoch time to normal time 

	Parameters
	----------
	time : Integer
		Epoch Time

	Returns
	-------
	normal : String
		General Time
	"""
	value = datetime.datetime.fromtimestamp(time)
	Normal = value.strftime('%Y-%m-%d %H:%M:%S')
	print(normal)
	return normal

if __name__ == '__main__':
	time = 1506065040 #input sample
	epoch2time(time)
	
# == END =======================================================================