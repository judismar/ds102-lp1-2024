from random import randint

estudantes = ['Artur Assis', 'Arthur Moretti', 'Arthur do Vale', 'Alexandra', 'Caio', 'Cassio', 'Daniel', 'Dylan', 'Manu', 'Fernanda', 'Guilherme', 'Gustavo', 'Tomas', 'Gabriel', 'Isaac', 'Judce', 'João Pedro Domingos', 'João Pedro Santos', 'Jão', 'Julia', 'Paulo', 'Pedro', 'Pedro Gomes', 'Pedro Henrique Vieira', 'Pedro Henrique Lyra', 'Pedro Richard', 'Ramon', 'Vitória', 'Wallace', 'Lúcio', 'Letícia', 'João Gabriel']

#Enquanto houver estudante na lista, faça:
while len(estudantes) > 0: #length: comprimento, tamanho
    n = len(estudantes)
    indice = randint(0, n - 1)
    estudante = estudantes.pop(indice)
    print(estudante)
    input()
