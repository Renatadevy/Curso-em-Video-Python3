#14 Escreva um programa que converta uma temperatura digitada em °C e converta para °F

print('-=-' *10)
print('CONVERSOR DE TEMPERATURA EM °C')
print('-=-'*10)

c = float(input('Digite a temperatura em °C: '))
f = 32 + (c * 1.8)
print('A temperatura de {}°C corresponde a {}F°'.format(c, f))

