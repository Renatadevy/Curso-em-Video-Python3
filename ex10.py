#10 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

real = float(input('Quanto você tem na carteira? R$ '))
dolar = real / 4.92
print('Com R${:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))


