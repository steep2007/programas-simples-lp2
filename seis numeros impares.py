num = int(input("Digite um numero:"))
num = num%2
for n in range(num,num+12):
  r = n%2
  if r==1:
    print("numeros: {}".format(n))