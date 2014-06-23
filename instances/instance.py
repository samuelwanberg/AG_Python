#! -*- coding: utf-8 -*-

#import numpy as np
import re
import sys
from math import sqrt,pow
import os


class Evaluate(object):

	def __init__(self,name):

		self.info = {}
		self.x = []
		self.y = []
		self.edgeDist = []
		self.optimal = 0
		self.setInstance(name)

	def setInstance(self,name):

		with open(name) as f:

			dados = map(str.split,map(lambda x: x.translate(None,"?!/;:"),map(str.strip,f.readlines())))
			dics = filter(lambda x: x[0]in ['NAME','TYPE','DIMENSION','EDGE_WEIGHT_TYPE'],dados)
			for dic in dics:
				self.info[dic[0]] = dic[1]
			coords = filter(lambda x: re.match(r"^[\d]+$",x[0]),dados)
			self.x =[ float(i[1]) for i in coords]
			self.y =[ float(i[2]) for i in coords]

			if len(self.info) != 4 or len(self.x)  != len(self.y):
				print('Instancia ',name,' nao contem todas as informacoes')
				sys.exit()

			self.NCity= int(self.info['DIMENSION'])

			with open(os.getcwd() + r'/instances/optimal.txt') as f2:
				value =filter(lambda x: x[0]==self.info['NAME'],map(str.split,map(lambda i: i.translate(None,"?.!/;:"),map(str.strip,f2.readlines()))))
				if bool(value):
					self.optimal = int(value[0][1])
				else:
					print('Valor otimo nao cadastrado')
					sys.exit()

			if self.info['EDGE_WEIGHT_TYPE'] == 'EUC_2D':

				self.edgeDist = [[ (sqrt(pow((self.x[i] - self.x[j]),2)+pow((self.y[i] - self.y[j]),2)) + 0.5)  for j in range(self.NCity)] for i in range(self.NCity)]
			elif self.info['EDGE_WEIGHT_TYPE'] == 'ATT' :

				for i in range(self.NCity):
					self.edgeDist.append([0] * self.NCity )
					for j in range(self.NCity):
						r = sqrt((pow(self.x[i]-self.x[j],2) + pow(self.y[i]-self.y[j],2))/10.0)
						t = int(r)
						if float(t) < r : self.edgeDist[i][j] = t+1
						else: self.edgeDist[i][j] = t
			elif self.info['EDGE_WEIGHT_TYPE'] == "CEIL_2D" :

				self.edgeDist =[[ceil(sqrt(pow(self.x[i] - self.x[j],2) + pow(self.y[i] - self.y[j],2))) for j in range(self.NCity)] for i in range(self.NCity)]
			else:
				print "EDGE_WIEGHT_TYPE is not supperted"
				return False

	def cost(self,ind):

		c = [ self.edgeDist[ind[i]-1][ind[i+1]-1] for i in range(len(ind)-1)]
		c.append(self.edgeDist[ind[-1]-1][ind[0]-1])
		ind.setValue(sum(c))
		return ind

	def __repr__(self):
		return '<Instance Name: {0} >'.format(self.info['NAME'])
