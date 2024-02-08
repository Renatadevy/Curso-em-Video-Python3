#31 Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem do ônibus cobrando 0,50R$ por Km para viagens de até 200kM e r$ 0,45 para viagens mais longas.


distancia = int(input('Digite a distância percorrida: '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))

if distancia <= 200:
    preço1 = distancia * 0.50
    print('Valor a pagar R${:.2f}'.format(preço1))
else:
    preço2 = distancia * 0.45
    print('Valor a pagar R$ {:.2f}'.format(preço2))


