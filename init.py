#! *-*coding:utf-8-*-

import random
import sys
from instances.read import Reads
from  results.Result import Result
from Genetic_Algorithms import Main
from  multiprocessing import Pool,Process
#import threading import Thread

"""
def  mainAG():

	'''
		pypy init.py n_interacoes n_pop tx_rep tx_mult
	'''

	tx_r = 80
	tx_m= 0.05
	trials = 10
 	instances = Reads()

 	print('********* Iniciando Algortimo *********')

 	for instance in instances:
		ni =  int(instance.info['DIMENSION'])/2
		ni  = filter(lambda x: x%2 == 0, [ni, ni+1])[0]
	
		ngmax = ni * 10
		result = Result(instance)
		print('Configuracao inicial N_Interacoes: {0} Tam_POP: {1} TX_R {2} TX_M {3}'.format(ngmax,ni,tx_r,tx_m))
		Main.main(instance,ni,ngmax,tx_r,tx_m,result,trials)



if __name__ == '__main__':

	mainAG()

"""

def  mainAG(instance):

	'''
		pypy init.py n_interacoes n_pop tx_rep tx_mult
	'''
	tx_r = 80
	tx_m= 0.05
	trials = 10
	print('********* Iniciando Algortimo *********')
 	ni =  int(instance.info['DIMENSION'])/2
 	print(ni)
	ni  = filter(lambda x: x%2 == 0, [ni, ni+1])[0]
	print(ni)
	ngmax = ni * 100
	result = Result(instance)
	print('Configuracao inicial N_Interacoes: {0} Tam_POP: {1} TX_R {2} TX_M {3}'.format(ngmax,ni,tx_r,tx_m))
	Main.main(instance,ni,ngmax,tx_r,tx_m,result,trials)


if __name__ == '__main__':

	instances = Reads()
	p = Pool()
	p.map(mainAG,instances)
	p.close()
	p.join()

"""
def  mainAG(instance):

	'''
		pypy init.py n_interacoes n_pop tx_rep tx_mult
	'''
	tx_r = 80
	tx_m= 0.05
	print('********* Iniciando Algortimo *********')
 	ni =  int(instance.info['DIMENSION'])/2
 	print(ni)
	ni  = filter(lambda x: x%2 == 0, [ni, ni+1])[0]
	print(ni)
	ngmax = ni * 100
	result = Result(instance)
	print('Configuracao inicial N_Interacoes: {0} Tam_POP: {1} TX_R {2} TX_M {3}'.format(ngmax,ni,tx_r,tx_m))
	Main.main(instance,ni,ngmax,tx_r,tx_m,result)


if __name__ == '__main__':

	instances = Reads()
	print('Aqui')
	p = Pool()
	p.map(mainAG,instances)
	p.close()
	p.join()
"""
