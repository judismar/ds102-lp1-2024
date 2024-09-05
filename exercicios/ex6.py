saldo = 200

while True: #Enquanto Verdadeiro:
    valor = int(input("Informe o valor do saque: "))
    if valor == 2 or valor == 5 or valor == 10 or valor == 50 or valor == 100:
        saldo -= valor
        print("Saque bem-sucedido. Novo saldo:", saldo)
    else:
        print("Saque mal-sucedido.")
