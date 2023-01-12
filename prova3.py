money=0.0
resposta = 0
lista_compras = []
while (resposta!=5):
    resposta = input('escolha um produto 1-iphone 2-chuchu 3-coquinha 4-finalizar')
    if(resposta=='1'):
        money=money+12000.0
        lista_compras.append("iphone")
    if (resposta == '2'):
        money = money + 0.50
        lista_compras.append("chuchu")
    if (resposta == '3'):
        money = money + 3.0
        lista_compras.append("coquinha")
    if(resposta=='4'):
        print ('lista de compra: {} \n valor total: {}' .format(lista_compras,money))
        break
