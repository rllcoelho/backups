#!/usr/bin/python
import os
from glob import glob

#Percorre recursivamente por todos os arquivos dentro de /media/backup/ (os.walk()) e identifica, dentre esses arquivos, os que sao backups. x eh a lista que eh retornada a cada iteracao de os.walk(), e a posicao 0 eh o caminho para o diretorio do arquivo
bkps = [y for x in os.walk("/media/backup/") for y in glob(os.path.join(x[0], '*-bkp-*'))]
#Identifica os arquivos aos quais pertencem os backups
nomes = set([arq[:arq.find('-bkp-')] for arq in bkps])
for nome in nomes:
	#Agrupa os backups por arquivo
	related = [x for x in glob(nome + '-bkp-*')]
	#Ordena os backups por tempo de modificacao. Como parametro da funcao de ordenacao, foi passada uma expressao lambda, ou funcao anonima, que recebe como parametro um item da lista e extrai das suas informacoes de status o seu tempo de modificacao.
	related.sort(key=lambda x: os.stat(x).st_mtime)
	'''Havia uma outra possibilidade:
			related.sort(key=lambda x: x[-10:])
		Isso ordenaria os backups pelos 10 ultimos caracteres, que correspondem ao tempo em que o backup foi feito, em segundos.
		Ou tambem, utilizar o tempo de criacao (st_ctime), ao inves do tempo de modificacao (st_mtime)'''
	if len(related) > 2:
		#Se houver mais de 2 backups, os mais antigos sao removidos
		for f in related[:-2]:
			os.remove(f)

