lista = 'abacate'
tamanho = len(lista)
a = ''
b = ''
c = ''
for i in range(0,tamanho):
    if lista[i]=='a':
        a = lista[i]
    if lista[i]=='b':
        b = lista[i]
    if lista[i]=='c':
        c = lista[i]
        if lista[i]=='a' and lista[i]=='b' and lista[i]=='c':
            print('tem as letras {}' .format(lista[i]))
        else:
           print('n tem')
