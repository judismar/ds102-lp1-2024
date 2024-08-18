from mundo import gera_mundo
from robo import efetua_passo

#O trabalho será sobre implementar um algoritmo (programa) em Python, o qual fará duas tarefas.

#gera_mundo tem um único argumento: o tamanho do mundo, o qual deve ser maior que 0. A função retorna um mundo, para ser usado na função "efetua_passo".
marte = gera_mundo(50)
p_robo = 24
nome_robo = "R2D2"
while True:
    dir = input("Escolha a direção: ")
    passo = int(input("Quantas casas o " +  nome_robo + " vai andar?\n"))
    #efetua_passo tem como argumentos a posição atual do robô, o mundo onde vai andar, a direção ('esquerda' ou 'direita') e a quantidade de passos que vai dar.
    #O robô para ao chegar no fim do mundo, em ambas as direções. Nada impede que ele continue andando para outra direção, a seguir.
    #Esquerda pode ser 'e' e direita 'd'. Se algo diferente for informado, ele irá para a esquerda.
    #Note que efetua_passo não atualiza a posição do robô. Foi necessário fazer isso logo abaixo.
    efetua_passo(p_robo, marte, dir, passo)
    if dir == 'd' or dir == 'direita':
        p_robo += passo
    else:
        p_robo -= passo
