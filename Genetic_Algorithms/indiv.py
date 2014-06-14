# -*- coding:utf-8 -*-

class Indiv(object):

	def __init__(self,tour,cost=0):
		self.tour = tour
		self.cost = cost

	def setValue(self,cost):
		self.cost = cost

	def value(self):
		return self.cost

	def __repr__(self):		
		return '<tour {0} \n Custo:{1}>'.format(self.tour,self.cost)

	def __len__(self):
		return len(self.tour)	

	def __getitem__(self,pos):
		return self.tour[pos]
	
	def __setitem__(self,pos,valor):
		self.tour[pos] = valor	
