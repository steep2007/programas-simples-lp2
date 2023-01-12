lista=[-1,-2,-4,5]
tamanho = len(lista)
for i in range(tamanho):
    if lista[i] > 0:
        print('seu credito é: {}'.format(lista[i]))
    else:
        print('seu debito é: {}'.format(lista[i]))