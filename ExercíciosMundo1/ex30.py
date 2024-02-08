#30 Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('Digite um número: '))

resuldado = num %2

if resuldado == 0:
    print('é PAR'.format(num))
else:
    print('é IMPAR'.format(num))