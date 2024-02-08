#32 Faça um programa que leia um ano qualquer e mostre se é um ano BISSEXTO.

ano = int(input('Que ano quer analisar? '))
if ano  % 4 == 0 and ano % 100 != 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))

