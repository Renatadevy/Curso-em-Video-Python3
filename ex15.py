#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado. Calcule o preço a pagar,sabendo que o carro custa r$60 por dia e r$ 0,15 por Km rodado. 

dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km percorridos? '))
pago =  (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.0f}'.format(pago))

