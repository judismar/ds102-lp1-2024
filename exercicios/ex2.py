pos = int(input("Informe a nova posição do robô: "))
if pos < 0:
    pos = 0
if pos > 99:
    pos = 99
print("Posição nova do robô: ", pos)
