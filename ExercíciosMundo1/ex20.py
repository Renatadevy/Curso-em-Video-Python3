#20 O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = input('Aluno(a): ')
a2 = input('Aluno(a): ')
a3 = input('Aluno(a): ')
a4 = input('Aluno(a): ')

lista = [a1, a2, a3, a4]

shuffle(lista)

print('Ordem de apresentação do trabalho: ')
print(lista)