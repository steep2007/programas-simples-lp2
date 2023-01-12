palavra = input('digite uma palavra')
letra = input('digite uma letra')
tamanho = len(palavra)
for i in range(0,tamanho):
    if palavra[i]==letra:
        print('tem a letra no indice: {}' .format(i))
    else:
       print('0')
