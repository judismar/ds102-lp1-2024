from random import randint

#'cara' é representado por 1
#'coroa' é representado por 2
escolha = input("Escolha entre cara ou coroa: ")
resultado = randint(1, 2)
if resultado == 1:
    resultado = "cara"
else:
    resultado = "coroa"
print("Resultado:", resultado)
if escolha == resultado:
    print("Você venceu!")
else:
    print("Você perdeu...")
