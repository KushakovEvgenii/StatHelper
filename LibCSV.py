'''This module is used for work with import CSV-file'''

import csv

class CSV:
	def __init__(self):
		pass
	def read(self,path):
		'''Program open CSV-file and append data in two-dimensional massive'''
		with open(path) as f:
		    read_file = csv.reader(f, delimiter=';' or ',')
		    massive = []
		    for row in read_file:
		    	massive.append(row)
		    return massive

csv_module = CSV()
file = csv_module.read('F:/Проекты/addresses.csv')