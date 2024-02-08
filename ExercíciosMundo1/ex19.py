#19 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles(alunos) e escrevendo o nome do escolhido. 

from random import choice
a1 = str(input('Aluno(a): '))
a2 = str(input('Aluno(a): '))
a3 = str(input('Aluno(a): '))
a4 = str(input('Aluno(a): '))
lista = [a1,a2,a3,a4]
print('O aluno escolhido a apagar o quadro será: {}'.format(choice(lista).upper()))