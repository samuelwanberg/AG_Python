#-*-coding:utf-8 -*-

import os,sys
import re ,time
from instance import Evaluate


class Reads(object):

	dir_name = os.getcwd() + r'/instances/files/'
	instances = []

	def __init__(self):

		print('<-Lendo arquivos de instacias-> \n')
		assert os.path.exists(self.dir_name) ,'<< Erro: Dir Name {0} not exists >>'.format(self.dir_name)
		self.filenames=[line for line in os.listdir(self.dir_name) if re.match(r'.[a-zA-z0-9]*\.tsp$',line,re.M|re.I)]
		print('<-Instacias registradas  ')
		print(self.filenames)

		with open(os.getcwd() + r'/instances/read.log','a') as f:
			f.write( time.strftime("%b %d %Y %H:%M:%S") + ': Instacias Resgistradas\n')
			f.write(str(self.filenames)+'\n')

		if len(self.filenames) > 0:
			self.instances = [ Evaluate(str(self.dir_name+name)) for name in self.filenames]
			with open(os.getcwd() + r'/instances/read.log','a') as f:
				f.write( time.strftime("%b %d %Y %H:%M:%S") + 'Procedimento Finalizado com sucesso \n\n')
		else:
			print('No instance in files dir')
			with open(os.getcwd() + r'/instances/read.log','a') as f:
				f.write( time.strftime("%b %d %Y %H:%M:%S") + 'Procedimento Falho a executar operacao : Sem instacionas no diretorio file\n\n')
			sys.exit()

		print('Operacao de realizar leitura de instacias executada')

	def __repr__(self):
		return 'Instaces Names : {0} '.format([ str(i)+'\n' for i in self.instances])

	def __len__(self):
		return len(self.instances)

	def __getitem__(self,pos):
		return self.instances[pos]

	def __setitem__(self,pos,valor):
		self.instances[pos] = valor





