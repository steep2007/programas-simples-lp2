c1 = input('digite um caracter')
c2 = input('digite outro caracter')
frase = input('digite uma frase')
tam = len(frase)
quantidade = 0
quantidade2 = 0
for i in range(0,tam):
    if frase[i] == c1:
        print('achei o caracter {}' .format(c1))
        quantidade = quantidade + 1
    if frase[i] == c2:
        print('achei o caracter {}' .format(c2))
        quantidade2 = quantidade2 + 1
print('achei o {} {} vezes e o caracter {} {} vezes' .format(c1,quantidade,c2,quantidade2))
