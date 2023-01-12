num = float(input('digite um num uh'))
if num>=0 and num<=25:
    print('Intervalo [0,25]')
if num>25 and num<=50:
    print('Intervalo (25,50]')
if num>50 and num<=75:
    print('Intervalo (50,75]')
if num>75 and num<=100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')