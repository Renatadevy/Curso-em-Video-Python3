#18
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente. 

#convertendo para radianos ... 
import math
from time import sleep

angulo = int(input('Digite o ângulo que você deseja: '))
print('calculando...')
sleep(3)

seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))




#importando apenas radians, sen , cos e tan:

from math import radians, sin, cos, tan
from time import sleep
angulo = int(input('Digite o ângulo desejado: '))
print('Calculando...')
sleep(1)

seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))