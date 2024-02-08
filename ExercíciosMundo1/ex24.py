#24 Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: '))
print('A cidade começa com "SANTO"? ', cidade[:5].upper() == 'SANTO' )

