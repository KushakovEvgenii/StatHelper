'''This module is used for import to Excel-files'''

import pandas as pd

class Export:
	def __init__(self):
		pass
	def createfile(self,name):
		file_name = name+".xls"
		file = open(file_name, "w+")
		file.close()
		return file_name
	def adddatatofile(self,file_name,data,name,i):
		dataframe = pd.DataFrame(data)
		dataframe.to_excel(file_name,sheet_name = name,index = i)

export = Export()
file_name = export.createfile("123")
a = ({'Numbers' : ['1','2','3','4','5']})
export.adddatatofile(file_name,a,'Test',False)