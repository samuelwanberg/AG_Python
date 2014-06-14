# -*- coding:utf-8 -*-
from random import random,choice


class Mutacao:


	def __init__(self,filhos,pm):
		self.filhos = filhos
		self.pm = pm

	def setFilhos(self,filhos):
		self.filhos=filhos

	def mutacao(self):
		n_mut=0
		filhosM=[]

		for filho in self.filhos:
			prop = random()

			if prop <= self.pm:
				n_mut = n_mut + 1
				tam_p = len(filho)
				posicoes = list(range(tam_p))
				p1 = choice(posicoes)
				del posicoes[p1]
				p2 = choice(posicoes)
				filho[p1],filho[p2] = filho[p2],filho[p1]

			filhosM.append(filho)
		return filhosM,n_mut

