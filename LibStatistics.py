'''This module is used for work with statistics'''

import numpy as np

class Statistics:
	def __init__(self):
		pass
	def showcommondata(self,need_massive):
		massive = np.array(need_massive, float)
		print(massive.min(),massive.max(),np.median(massive),np.corrcoef(massive),np.cov(massive))