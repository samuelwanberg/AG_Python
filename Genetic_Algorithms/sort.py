#! -*- coding: utf-8 -*-



def partition(v, left, right):
    i = left
    for j in range(left + 1, right + 1):
        if v[j].cost < v[left].cost: # Se um elemento j for menor que o pivo
            i += 1 # .. incrementa-se i
            v[i], v[j] = v[j], v[i] # .. e troca o elemento j de posicao o elemento i
    v[i], v[left] = v[left], v[i] # O pivo e' colocado em sua posicao final
    return i
 
def quicksort(v, left, right):
    if right > left: # Verifica se a lista tem 2 ou mais itens
        pivotIndex = partition(v, left, right) # Pega a posicao do pivo
        quicksort(v, left, pivotIndex - 1) # Ordena recursivamente os itens menores que o pivo
        quicksort(v, pivotIndex + 1, right) # Ordena recursivamente os itens maiores que o pivo
 
def heapsort(lst):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
# in pseudo-code, heapify only called once, so inline it here
  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child].cost < lst[child + 1].cost:
      child += 1
    if lst[root].cost < lst[child].cost:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break 
