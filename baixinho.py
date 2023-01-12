# altura = ['1,70','1,50','1,80']
# menor = min(altura)
# print(menor)

altura = [1.70, 1.50, 1.80, 0.8]
tam = len(altura)
menor = 999999999
for i in range(0, tam):
    if altura[i] < menor:
        menor = altura[i]
print(menor)
