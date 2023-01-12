#linha1 = ['','','']
#linha2 = ['','','']
#linha3 = ['','','']
#matriz = []
#matriz.append(linha1)
#matriz.append(linha2)
#matriz.append(linha3)
#for i in matriz:
    #corx = int(input('qual a posição?'))
   # cory = int (input ('qual a posição?'))
  #  jogada = input('qual a sua jogada?')
  #  matriz.append(matriz.insert([corx] [cory],jogada))
  #  print(matriz)


matriz = [[],[],[]]
for l in range(0,3):
        for c in range(0,3):
                matriz[l].append(input(f"Digite um valor para [{l},{c}]: "))
                if matriz[0][0] == 'o' and matriz[0][1] == 'o' and matriz[0][2] == 'o':
                     print ('jogador o venceu')
#print('-='*30)
#for l in range(0,3):
 #       for c in range(0,3):
  #              print(f'[{matriz[l][c]:^3}]', end='')
   #     print()