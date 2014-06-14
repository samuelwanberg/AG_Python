# -*- coding: utf-8 -*-
from random import randint,choice,shuffle 
from indiv import Indiv
import random
from itertools import groupby

def crossover_PMX(pai1, pai2):

	ind1 = pai1[::]
	ind2 = pai2[::]
	size = min(len(ind1), len(ind2))
	p1, p2 = [0]*size, [0]*size
	
	for i in xrange(size):
		p1[ind1[i]-1] = i 
		p2[ind2[i]-1] = i 
	
	cxpoint1 = random.randint(0, size)
	cxpoint2 = random.randint(0, size - 1)
	if cxpoint2 >= cxpoint1:
		cxpoint2 += 1
	else: 
		cxpoint1, cxpoint2 = cxpoint2, cxpoint1

	for i in xrange(cxpoint1, cxpoint2):
		temp1 = ind1[i] 
		temp2 = ind2[i] 

		ind1[i], ind1[p1[temp2-1]] = temp2, temp1
		ind2[i], ind2[p2[temp1-1]] = temp1, temp2

		p1[temp1-1], p1[temp2-1] = p1[temp2-1], p1[temp1-1]
		p2[temp1-1], p2[temp2-1] = p2[temp2-1], p2[temp1-1]

	return Indiv(ind1), Indiv(ind2)

def crossover_Cycle(pai1,pai2):

	assert len(pai1) == len(pai2) , "A quantidade de crosmossomos entre o pai1 e o pai2 são diferentes ou nao formam pares!"
	ind1 = pai1[::]
	ind2 = pai2[::]
	i = choice(ind1)
	index = ind1.index(i)

	while True:
		ind1[index],ind2[index] = ind2[index],ind1[index]
		elem = ind1[index]

		if elem == i:
			break
		index = pai1[::].index(elem)
	return Indiv(ind1),Indiv(ind2)

def crossover_OX1(parent1,parent2):
			
	pai1 = parent1[::]
	pai2 = parent2[::]
	#Sorteio dos pontos de cruzamento
	assert len(pai1) == len(pai2) , "A quantidade de crosmossomos entre o pai1 e o pai2 são diferentes ou nao formam pares!"
	tam_c = len(pai1)  # armazena o tamanho do cromosso
	p1 = randint(1, int(tam_c/2) )      #definindo o ponto1 aleatoriamente
	p2 = randint(int(tam_c/2), tam_c-2) #definindo o ponto2 aleatoriamente
	inverso_pai1 = pai1[p2+1:] + pai1[:p2+1]	
	inverso_pai2 = pai2[p2+1:] + pai2[:p2+1]
	filho1 = [ j for j in inverso_pai2 if not j in pai1[p1:p2+1]]
	filho2 = [ j for j in inverso_pai1 if not j in pai2[p1:p2+1]]	
	tam = len(pai1[p2+1:])
	filho1 =  filho1[tam:] + pai1[p1:p2+1] + filho1[:tam]
	filho2 =  filho2[tam:] + pai2[p1:p2+1] + filho2[:tam] 
	return Indiv(filho1),Indiv(filho2)	

def crossover_OX2(parent1,parent2):	
	
	assert len(parent1) == len(parent2), "A quantidade de crosmossomos entre o pai1 e o pai2 são diferentes ou nao formam pares!"
	parent1 = parent1[::]
	parent2 = parent2[::]
	ind1 = parent1[::]
	ind2 = parent2[::]
	quantTrocas = randint(1,len(parent1)-2)
	indices = list(range(len(parent1)))
	shuffle(indices)
	indices = indices[:quantTrocas]
	indice_ch1 = []
	indice_ch2 = []
	for i in indices:
		indice_ch1.append(parent1.index(parent2[i]))
		indice_ch2.append(parent2.index(parent1[i]))
	indice_ch1.sort()
	indice_ch2.sort()
		
	for i in range(len(indices)):
		ind1[indice_ch1[i]] =  parent2[indices[i]]
		ind2[indice_ch2[i]] =  parent1[indices[i]]
	
	return Indiv(ind1) , Indiv(ind2)	


#Utilizado no crossover_ER	
def remove_repitidos_lista(l):		
	t = []
	[ t.append(item)   for item in l if not t.count(item)]
	return t

def crossover_POS(parent1,parent2):
	pai1 = parent1[::]
	pai2 = parent2[::]
	assert len(pai1) == len(pai2), "A quantidade de crosmossomos entre o pai1 e o pai2 são diferentes ou nao formam pares!"
	quantTrocas = randint(1,len(pai1)-1)
	indices = list(range(len(parent1)))
	shuffle(indices)
	posicoes = indices[:quantTrocas]
	filho1 , filho2 = pai1[::], pai2[::]
	#parte3
	for j in posicoes:
		pai1.remove(filho2[j])
		pai2.remove(filho1[j])
	#parte4
	for j in range(len(filho1)):
		if not j in posicoes:
			filho1[j] = pai2.pop(0)
			filho2[j] = pai1.pop(0)
	return Indiv(filho1),Indiv(filho2)			         

def crossover_ER(parent1,parent2):
			
	mapa_arestas = {}
	p1 =parent1[::]
	p2 = parent2[::]
	filho = []
	#Constroi o mapa de aresta referente aos dois pais 
	n = len(p1) -1
	result = list(map(lambda j:  [ p2[ p2.index(p1[j]) - 1], p2[ p2.index(p1[j]) - n ]] + [ p1[j-1], p1[j - n] ], range(n+1)))
	for k in range(len(result)):
		mapa_arestas[p1[k]] = remove_repitidos_lista(result[k])

	#Selecionada cidade corrente inicial
	#Passo 1   		
	curr_city = choice(p1)
			
	while(True):

		filho.append(curr_city)
		#Aqui removemos a cidade atual da lista de aresta ao lado esquedor na tabelo de arestas que a cidade atual esta interligada nos pais
		z = list(filter(lambda x: curr_city in mapa_arestas[x],list(mapa_arestas.keys())))
		[ mapa_arestas[j].remove(curr_city) for j in z ]
		#Passo 4 seleciona proxima cidade corrente que tenha o menor numero de aresta no mapa de aresta 
		if not mapa_arestas[curr_city] == []:	
			list_indices = [ len(mapa_arestas[j])   for j in mapa_arestas[curr_city]]
			aux = curr_city
			curr_city =  mapa_arestas[curr_city][list_indices.index(min(list_indices))]
			mapa_arestas.pop(aux)
		else:
			mapa_arestas.pop(curr_city)	
			if len(mapa_arestas.keys()) != 0:
				curr_city =  choice(list(mapa_arestas.keys()))
			else:						
				break							
			
	return Indiv(filho)		
			