#29 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar r$ 7R$  por cada km acima do limite.

velocidade = int(input('Velocidade: '))
multa = (velocidade - 80) * 7
if velocidade >80:
    print('Multado(a)!')
    print('Valor da sua multa: R$ {:.2f}'.format(multa))
print('Tenha um ótimo dia, dirija com atenção.')

