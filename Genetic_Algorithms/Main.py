#! -*-coding: utf-8 -*-
import random
import sys
import instances.read
from Genetic_Algorithms import *
from Roleta import Roleta
from Mutacao import Mutacao
from Reinsercao import Reinsercao
from indiv import Indiv
import time
from sort import *
from crossovers import *

class GA:

	def __init__(self,instance,nOfPop,nInter,txR,txM,result):

		self.instance = instance
		self.dimension = int(self.instance.info['DIMENSION'])
		self.nOfPop = nOfPop
		self.nInter = nInter
		self.txR = txR
		self.txM = txM
		self.result = result

	def geraP_Inicial(self,citys,len_pop):

		tour = range(1,citys+1)
		pop = []      # Lista que ira armazenar populacao de cromossomos inicial
		for i in range(len_pop):
			random.shuffle(tour)   # Embaralha aleatoriamente o cromossomo
			aux =  tour[::]  	#  lista do cromossomo auxiliar
			indv = Indiv(aux)	# armazena cromossomo na populacao
			pop.append(indv)
		pop = self.fitness(pop)
		return pop

	def fitness(self,pop):
		return [self.instance.cost(indiv)  for indiv in pop]

	def DoIt(self,crossType,trials):
		
		c_trials = 1
		while c_trials <= trials:  
			
			self.pop = self.geraP_Inicial(self.dimension,self.nOfPop)
			self.pop = heapsort(self.pop)
			bestTour  = self.pop[0].tour
			bestCost  = self.pop[0].value()			
			i = 1
			while i < self.nInter and bestCost >= self.instance.optimal:
				
				Pc = Roleta(self.pop,self.txR).roleta()
				if crossType == "PMX":
					Pc  = map(lambda x: crossover_PMX(Pc[x],Pc[x+1]),range(0,len(Pc),2))										
				elif crossType == "Cycle":					
					Pc  = map(lambda x: crossover_Cycle(Pc[x],Pc[x+1]),range(0,len(Pc),2))		 
				elif crossType == "OX1":
					Pc  = map(lambda i: crossover_OX1(Pc[i],Pc[i+1]),range(0,len(Pc),2))
				elif crossType == "OX2":
					Pc  = map(lambda i: crossover_OX2(Pc[i],Pc[i+1]),range(0,len(Pc),2))
		  		elif crossType == "POS":
		  			Pc  = map(lambda i: crossover_POS(Pc[i],Pc[i+1]),range(0,len(Pc),2))
				elif crossType == "ER":
					aux_Er = Pc[::]
					random.shuffle(aux_Er)
					Pc = Pc + aux_Er
					Pc  = map(lambda i: crossover_ER(Pc[i],Pc[i+1]),range(0,len(Pc),2))					
				else:
					print('Crossover Operation Fail ')
				aux = []
				if not crossType == "ER": 
					for itr in Pc:
						aux.append(itr[0])
						aux.append(itr[1])
					Pc = aux
					
				filhos,n_mut = Mutacao(Pc,self.txM).mutacao()
				self.fitness(filhos)
				self.pop = Reinsercao(self.pop,filhos).aplica_reinsercao()
				bestTour  = self.pop[0].tour
				bestCost  = self.pop[0].value()
				print('Instancia: {0} Crossover: {1} Interacao: {2} optimal: {3} beasCost: {4}'.format( self.instance.info['NAME'],crossType,i,self.instance.optimal,bestCost))				
			
				if bestCost <= self.instance.optimal:
					break
				
				i = i + 1

			'''Escrevendo Dados No Arquivo'''
			DATA_Result = "{0} {1} {2} {3}" .format(c_trials,i,bestCost,len(self.pop))
			DATA_Solution = "{0} {1} {2}\n{3}" .format(c_trials,i,bestCost,bestTour)
			self.result.saveBestSol(crossType,DATA_Solution)
			self.result.saveResult(crossType,DATA_Result)
			c_trials = c_trials +1	
		return True

def main(instance,nOfPop,nInter,txR,txM,result,trials):

	#crossovers = ['ER']
	crossovers = ['PMX','Cycle','OX1','OX2','POS','ER']
	for cross in crossovers:
		print('Instancia: {0} Crossover {1}'.format(instance.info['NAME'],cross ))
		Ag = GA(instance,nOfPop,nInter,txR,txM,result)
		Ag.DoIt(cross,trials)
	print('Fim de Teste para execucao ')
