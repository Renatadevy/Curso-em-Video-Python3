#22Crie  um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas as letras maiúsculas
#-O nome com todas minúsculas
#-Quantas letras ao todo (sem considerar espaços
#-Quantas letras tem o primeiro nome.


nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas: {}'.format(nome).upper())
print('Seu nome em letras minúscilas: {}'.format(nome).lower())
print('Seu nome tem {} letras'.format(len(nome)- nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(separa[0])))