saldo = int(input("Informe quanto tem de dinheiro: "))
print(saldo)
menu = input("--Farmácia--\n\nDorflex: 14,90\nDipirona: 20,00\nParacetamol: 9,99\nSair\n")

while menu == "Dorflex" or menu == "Dipirona" or menu == "Paracetamol":
    if menu == "Dorflex":
        saldo -= 14.90
    elif menu == "Dipirona":
        saldo -= 20
    elif menu == "Paracetamol":
        saldo -= 9.99
    print(saldo)
    menu = input("--Farmácia--\n\nDorflex: 14,90\nDipirona: 20,00\nParecetamol: 9,99\nSair\n")
