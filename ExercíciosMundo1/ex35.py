#35 Desenvolva um programa que leia o comprimento de três retas e diga ao usurário se elas podem ou não formar um triângulo

#Analisando triângulo 
r1 = float(input('Primeniro comprimento: '))
r2 = float(input('Segundo comprimento: '))
r3 = float(input('Terceiro comprimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')