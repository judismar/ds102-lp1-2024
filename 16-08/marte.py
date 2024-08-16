from mundo import gera_mundo
from robo import efetua_passo

marte = gera_mundo(50)
p_robo = 24
nome_robo = "R2D2"
while True:
    dir = input("Escolha a direção: ")
    passo = int(input("Quantas casas o " +  nome_robo + " vai andar?\n"))
    efetua_passo(p_robo, marte, dir, passo)
    if dir == 'd' or dir == 'direita':
        p_robo += passo
    else:
        p_robo -= passo
