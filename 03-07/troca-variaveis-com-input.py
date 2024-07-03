#Programa que troca o valor de duas variáveis, melhorado para o caso geral em que o usuário que interage com o programa escolhe o valor string/texto para cada variável.
#A função input() retorna o valor informado pelo teclado.

#Variáveis
var1 = input("Informe o valor da primeira variável: ")
var2 = input("Informe o valor da segunda variável: ")

#Algoritmo de 3 linhas.
temp = var1
var1 = var2
var2 = temp

#Verificação de corretude:
print(var1, var2)
