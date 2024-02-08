
#16 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.


from math import trunc
numero = float(input('Digite um número real Ex: 6.127\nr: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(numero, trunc(numero)))
