"""
							 SAVING DATA INTO CSV FORMAT
	* This format is used for many purposes, mainly for deep learning.
	* This type of file can be used to view data in MS Excel or any similar 
	  Application
"""
# == Imports ===================================================================

import csv
import sys

# == Initialisation Function ===================================================

def initialise_csvlog(filename, fields):
	"""
	Initilisation this function before using the Inserction function

	* This Function checks the data before adding new one in order to maintain
	  perfect mechanisum of insertion
	* It check the file if not exists then it creates a new one
	* if it exists then it proceeds with getting fields

	Parameters
	----------
	filename : String
		Filename along with directory which need to be created
	Fields : List
		Colomns That need to be initialised

	"""
	try :
		with open(filename,'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = csvreader.next()
			print("Data Already Exists")
			sys.exit("Please Create a new empty file")
			# print fields	
	except :
		with open(filename,'w') as csvfile:

			csvwriter = csv.writer(csvfile)
			csvwriter.writerow(fields)

# == Data Insertion Function ===================================================

def write_data_csv(filename, row_data):
	"""
	This Function save the Row Data into the CSV Created
	* This adds the row data that is Double Listed

	Parameters
	----------
	filename : String
		Filename along with directory which need to be created
	row_data : List
		Double Listed consisting of row data and coloumn elements in a list	
	"""
	with open(filename,'a') as csvfile:

		csvwriter = csv.writer(csvfile)
		csvwriter.writerows(row_data)

if __name__ == '__main__':
	"""
	This function is used to test the Feature Run it independently
	
	NOTE: DATA IN row_data MUST BE IN THE FOLLOWING DOUBLE LISTED AS SHOWN
	"""
	filename = "TestCSV.csv"
	fields = ["sno","Name","Work","Department"]
	#Init
	initialise_csvlog(filename,fields)
	#Add Data
	row_data = [["1","Jhon","Coder","Pythonic"]]
	write_data_csv(filename,row_data)

# == END =======================================================================