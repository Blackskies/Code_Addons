# == Imports ===================================================================
import datetime
# == Input Time ================================================================
time = 1506065040

value = datetime.datetime.fromtimestamp(time)
print(value.strftime('%Y-%m-%d %H:%M:%S'))
# == END =======================================================================