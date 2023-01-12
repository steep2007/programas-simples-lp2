numeros = input('Digite seus numeros')
tamanho = len(numeros)
for i in range(0,tamanho):
    if numeros[i]=='0':
        print('O zero aparece {}' .format(tamanho - 1))