import struct
import sys
import os

#Thaina Simoes Pires
#Organizacao e estrutura de arquivos
#Python 2.7.14

if len(sys.argv) != 2:
	tamBloco = int(input("Entre com o numero de linhas de cada bloco: "))
else:
	tamBloco = int(sys.argv[1])

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
print "Tamanho da Estrutura: %d" % registroCEP.size
f = open("cep.dat","rb+")
tam = os.path.getsize("cep.dat")/registroCEP.size
tamBlocos = []
qtdBlocos = tam / tamBloco
resto = tam - (tamBloco * qtdBlocos)
tamBlocos = [tamBloco] * qtdBlocos
if resto > 0:
	tamBlocos.append(resto)

def cmp ( ta, tb ):
	if ta[cepColumn] == tb[cepColumn]: return 0
	if ta[cepColumn] > tb[cepColumn]: return 1
	return -1

cont2 = 0 #variavel para conseguir se locomover no arquivo

for i in tamBlocos:	
	listOrdena = []
	cont = i #variavel para controlar o numero de leituras com a quantidade de linhas de cada bloco
	f.seek(cont2*registroCEP.size*i)
	while cont != 0:
		line = f.read(registroCEP.size)
		line_t = registroCEP.unpack(line)
		listOrdena.append(line_t)
		cont = cont - 1
	listOrdena.sort(cmp)
	f.seek(cont2*registroCEP.size*i)
	for j in range(i): 
		line_pack = registroCEP.pack(listOrdena[j][0], listOrdena[j][1], listOrdena[j][2], listOrdena[j][3], listOrdena[j][4], listOrdena[j][5], listOrdena[j][6])
		f.write(line_pack) #escreve no mesmo arquivo
	cont2 = cont2 + 1	
	listOrdena = []
print "Fim do programa"
f.close()
