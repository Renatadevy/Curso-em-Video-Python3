
#33 Faça um programa  que leia três números e mostre qual é o maior e qual é o menor.

from time import sleep
n1  = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

menor = n1 
if n2 < n1 and n3:
    menor = n2
if n3 < n1 and n2:
    menor = n2

maior = n1
if n2 > n1 and n3:
    maior = n2
if n3 > n1 and n2:
    maior = n3

print('...')
sleep(1)

print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))


