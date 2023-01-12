list = ['abra', 'feche']
l = []
l.append('4')
print(l)
#
l = l + ['chuchu', 'batata','4']
print(l)
#
print(l.index("chuchu"))
print(l[2])
l.extend(l + list)
print(l)
#slicing fatiamento 1:3 (seleciona de 1 até 2)
#print('fatiou ',{l:3})
print('fatiou', l[1:len(l)]) #da posição 1 até o final da lista
print('fatiar', l[2: ]) #da posição 2 até o final da lista
print('fatia final', l[ :3]) #do começo (0) até o indice 2
#
l.insert(0,'5')
print(l)
l.remove('chuchu')
print(l)
l.pop(0)
print(l)
l.pop(0 + 1 + 2)
print(l)