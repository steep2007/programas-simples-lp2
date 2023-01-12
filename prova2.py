frase = input ('Digite uma frase')
tam = len (frase)
quantidade = 0
for i in range (0, tam-3):
    if frase[i] == 'a' and frase[i+1] == 'i' and frase[i+2] == 'a' and frase[i+3] == 'i':
        print('verdadeiro')
        quantidade=quantidade+1
print('achei o -aiai- {} vezes' .format(quantidade))


