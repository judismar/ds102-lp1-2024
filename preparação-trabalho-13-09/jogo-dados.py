#Não joguem os 'bets', jogos de azar tem muito potencial para fazer mal à sua vida e à sua saúde!
from random import randint

pontuacao = 0

while True:
    print(pontuacao)
    print("\nJogo da casa:")
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    input()

    resultado_casa = dado1 + dado2
    print(dado1, dado2, resultado_casa)

    print("Seu jogo:")
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    input()

    resultado_jogador = dado1 + dado2
    print(dado1, dado2, resultado_jogador)

    if resultado_jogador > resultado_casa:
        print("Você venceu!!!")
        pontuacao += 200
    else:
        print("Você perdeu. :(")
        pontuacao -= 100
