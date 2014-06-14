# -*- coding: utf-8 -*-

from sort import heapsort
  

class Reinsercao:

	def __init__(self,pais,filhos):
		self.pais = pais 
		self.filhos = filhos
		
	def aplica_reinsercao(self):

		tam_pop = len(self.pais)
		self.p_final = self.pais[::] + self.filhos[::]
		self.p_final = heapsort(self.p_final)
		return self.p_final[:tam_pop]

