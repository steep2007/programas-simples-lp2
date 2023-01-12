grana = 45.0
resposta = 0
lista_compras = []
while (resposta!=-1):
    resposta = input('escolha um produto 1-arroz 2-feijao 3-macarrao')
    if(resposta=='1'):
        grana=grana-26.99
        lista_compras.append("Arroz")
    if (resposta == '2'):
        grana = grana - 8.99
        lista_compras.append("Feijão")
    if (resposta == '3'):
        grana = grana - 4.99
        lista_compras.append("MAcarrão")
    if(grana<=0):
        break
print(lista_compras)
