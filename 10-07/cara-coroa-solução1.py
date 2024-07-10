from random import randint

escolha = int(input("Informe 0 ou 1: "))
resultado = randint(0, 1)
print("Resultado: ", resultado)
if escolha == resultado:
    print('Você ganhou!')
else:
    print("Você perdeu...")
