def compraRoupa(dinheiro, roupa, valor):
    if dinheiro >= valor:
        if roupa == "vestido":
            print("Você comprou um " + roupa)
        else:
            print("Você comprou uma " + roupa)
        return dinheiro - valor
    else:
        print("Valor indisponível.")
        return dinheiro

dinheiro = 300.00
while True:
    menu = input("--Loja de roupas--\n1- Calça: 90.00\n2- Blusa: 29.90\n3- Camisa: 40.00\n4- Vestido: 129.99\n5- Sair\nEscolha o que quer comprar: ")
    if menu == '1':
        dinheiro = compraRoupa(dinheiro, "calça", 90.00)
    if menu == '2':
        dinheiro = compraRoupa(dinheiro, "blusa", 29.90)
    if menu == '3':
        dinheiro = compraRoupa(dinheiro, "camisa", 40.00)
    if menu == '4':
        dinheiro = compraRoupa(dinheiro, "vestido", 129.99)
    if menu == '5':
        break
    print(dinheiro)
