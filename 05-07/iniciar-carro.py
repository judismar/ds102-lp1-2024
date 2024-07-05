#Algoritmo de iniciar a direção de um carro, representado em Python.
#Digitar 1 significa "feito, pronto etc.".
#Introdução a if e else.

cinto = input("Colocou cinto? ")
marcha_neutra = input("Verificou a marcha? ")
ligar_carro = input("Ligou carro? ")
freio_de_mao = input("Destravou o freio de mão? ")
  
if cinto == '1' and marcha_neutra == '1' and ligar_carro == '1' and freio_de_mao == '1':
    print("Pode dirigir.")
else:
    print("Proibido dirigir assim!")
