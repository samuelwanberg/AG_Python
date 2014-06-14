#!  -*-coding: utf-8 -*-
import os

class Result(object):

	dir_name = os.getcwd() + r'/results/files/'

	def __init__(self,instance):

		self.instance = instance

		if not os.path.isdir(self.dir_name):
			os.mkdir(self.dir_name)

		name = self.instance.info['NAME'] + "/" 
		if not os.path.isdir(self.dir_name+name):
			os.mkdir(self.dir_name+name)
		self.dir_name +=name			
		
	def saveBestSol(self,crossoverName,dado):

		with open(self.dir_name+crossoverName+'_DATA_BestSol','a') as f:
			f.write(dado+'\n\n')
			

	def saveResult(self,crossoverName,dado):			
			
		with open(self.dir_name+crossoverName+'_DATA_Result','a') as f:
			f.write(dado+'\n\n')