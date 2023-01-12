idadedia = int(input("digite sua idade em dias "))
ano = idadedia-365
ano = ano%12
#if ano>365:
#    ano = ano + 1
mes = idadedia//30

print('ano: {} mes: {}' .format(ano,mes))

