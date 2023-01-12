from random import randrange
#import numpy as np

campo = []
tamanho = 15 #numero de posições do campo

#configurar o campo
for i in range(0,tamanho):
    campo.append('🌊')
   # print('[',campo[i],']',end='')

#navios -> * caiaque ** barco *** cruzeiro
#inserir o caiaque
posicao = randrange(0,tamanho)
campo[posicao] = '⛵'

#inserir barco
posicao = randrange(0,tamanho-1)
while(campo[posicao]=='⛵' or campo[posicao+1]=='⛵'):
    posicao = randrange(0,tamanho-1)
campo[posicao] = '⛵'
campo[posicao + 1] = '⛵'


#inserir cruzeiro
posicao = randrange(0, tamanho-2)
while (campo[posicao] == '⛵' and campo[posicao] == '⛵⛵' or campo[posicao+1]=='⛵' or campo[posicao+1]=='⛵'):
      posicao = randrange(0, tamanho-2)
campo[posicao] = '⛵'
campo[posicao + 1] = '⛵'
campo[posicao + 2] = '⛵'

print(f'CAMPO 1: {campo}')

campo2 = []
#configurar o campo
for i in range(0,tamanho):
    campo2.append('🌊')
   # print('[',campo2[i],']',end='')

#navios -> * caiaque ** barco *** cruzeiro
#inserir o caiaque
posicao = randrange(0,tamanho)
campo2[posicao] = '⛵'

#inserir barco
posicao = randrange(0,tamanho-1)
while(campo2[posicao]=='⛵' or campo2[posicao+1]=='⛵'):
    posicao = randrange(0,tamanho-1)
campo2[posicao] = '⛵'
campo2[posicao + 1] = '⛵'


#inserir cruzeiro
posicao = randrange(0, tamanho-2)
while (campo2[posicao] == '⛵' and campo2[posicao] == '⛵⛵' or campo2[posicao+1]=='⛵' or campo2[posicao+1]=='⛵'):
      posicao = randrange(0, tamanho-2)
campo2[posicao] = '⛵'
campo2[posicao + 1] = '⛵'
campo2[posicao + 2] = '⛵'
print(f'CAMPO 2: {campo2}')

##Jogadas

pont1=0
pont2=0
while True:

posicao = int (input ('Digite a posicao para lancar a bomba (0 a 14)'))
if posicao < 0 or posicao > tamanho - 1:
    exit ()
if campo2[posicao] == '⛵':
    print ('💣! Você acertou um barco 🪵')
    campo2[posicao] = '🌊'
else:
    print ('Errou! SPLASH 🌊')
if pont1>=6:
    print('UEPW VC VENCEU 🙌💫🤧')
    exit()

print ('Jogada do oponente')
posicao2 = randrange (0, tamanho - 1)  # IA burra, idiota, besta, tudo de ruim
if campo2[posicao2] == '⛵':
    print ('💣! Você acertou um barco 🪵')
    campo2[posicao2] = '🌊'
else:
    print ('Errou! SPLASH 🌊')
if pont1>=6:
    print('psraven 🥸🤓')
    exit()







