#28 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


from random import randint
from time import sleep
jogador = int(input('Em que número eu pensei? '))
computador = randint(0,5)
print('...')
sleep(2)

if jogador == computador:
    print('Você venceu! eu também pensei no número {}'.format(computador))
else:
    print('Eu venci! Eu pensei no número {} e não {}'.format(computador, jogador))
