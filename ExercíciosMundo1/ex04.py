#Faça um programa que leia algo pelo teclado e seu tipo primitico e todas as informações sobre ela. 

teclado = input('Digite algo: ')
print('O tipo primitivo de {} é: {}'.format(teclado, type(teclado)))
print('É um número?',teclado.isnumeric())
print('Tem é maiúsculo?', teclado.isupper())
print('É minúsculo?', teclado.islower())
print('Só tem espaços?', teclado.isspace())
print('Está capitalizada?', teclado.istitle())











