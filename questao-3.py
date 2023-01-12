numeros = [1,2,3,4,5]
pares = []
impares = []
num=0
num=len(numeros)
for i in range(0,num):
    a=numeros[i]%2
    if a==0:
        pares = numeros[i]
        print('lista pares [{}]'.format(pares))
    else:
        impares = numeros[i]
        print('lista impares [{}]'.format(impares))