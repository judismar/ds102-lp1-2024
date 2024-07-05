#Exercício: Escreva um programa que pede ao primeiro jogador para informar cara ou coroa. O segundo jogador então decide se caiu cara ou coroa que (usando input) para ver se o jogador 1 venceu. O jogador 2 nunca vence, apenas informa a face da moeda.

j1 = input("Escolha cara ou coroa: ")
j2 = input("Escreva qual face ficou pra cima: cara ou coroa? ")
print("Caiu", j2)
if (j1 == "cara" and j2 == "cara") or (j1 == "coroa" and j2 == "coroa"):
  print("Parabéns, você venceu!")
else:
  print("Você perdeu!")
