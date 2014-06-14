# -*-coding: utf-8 -*-

import sort
import random


class Roleta:

	def __init__(self,population,p_rep):
		self.populacao = population
		self.p_rep = p_rep
		self.sobreviventes = []

	def setIndividuos(self,populacao):
		self.populacao = populacao
		
	def setProbabilidadeRep(self,p_rep):
		self.p_rep = p_rep

	def roleta(self):
		lista_ord = self.populacao[::]
		lista_ord = sort.heapsort(lista_ord)
		lista_ord.reverse()
		roleta = []
		for i in range(len(lista_ord)):
			roleta = roleta + [i] * (i+1)
		self.indices = []
		quant =  int(len(lista_ord) * self.p_rep/100)
		quant = filter(lambda x: x % 2 ==0,[quant,quant+1])[0]
		i = 0
		while(i < quant):
			indice = random.choice(roleta)
			if not indice in self.indices:
				self.indices.append(indice)
			else:
				i = i -1
			i = i+1
		self.sobreviventes  = [  lista_ord[i] for i in self.indices ]
		return self.sobreviventes

	def __repr__(self):
		return "<Selecioandos: {0}>".format(self.sobreviventes)

	def __len__(self):
		return len(self.sobreviventes)

	def __getitem__(self,pos):
		return self.sobreviventes[pos]

	def __setitem__(self,pos,valor):	
		self.sobreviventes[pos] = valor










