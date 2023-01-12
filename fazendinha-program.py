alface = 40
mandioca = 200
planta = input("Digite a planta:")
dia = int(input("Digite o dia da colheita:"))
mes = int(input("Digite o mes:"))
if planta=='alface':
        dia = dia + alface
        dia = dia % 30
        mesp = mes + (dia + alface) // 30
        mesp = mesp % 12
        print("{}/{}".format(dia,mesp))
if planta=='quiabo' or planta=='repolho':
        tempo = 80
        dia = dia + tempo
        dia = dia % 30
        mesp = mes + (dia + tempo) // 30
        mesp = mesp % 12
        print("{}/{}".format(dia,mesp))
if planta=='repolho':
        dia = dia + repolho
        dia = dia % 30
        mesp = mes + (dia + repolho) // 30
        mesp = mesp % 12
        print("{}/{}".format(dia,mesp))
if planta=='mandioca':
        dia = dia + mandioca
        dia = dia % 30
        mesp = mes + (dia + mandioca) // 30
        mesp = mesp % 12
        print("{}/{}".format(dia,mesp))