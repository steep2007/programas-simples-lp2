l = [0,1,2,3,4,0,5]
tam = len(l)
num = int(input("digite um numero"))
quantidade = 0
for i in range(0,tam):
    if l[i]==num:
        print('tem seu numr')
        quantidade = quantidade+1
print('achei o {} {} vezes' .format(num,quantidade))


