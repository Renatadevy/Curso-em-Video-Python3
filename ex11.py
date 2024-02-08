#11 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidase de tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m qua...

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = alt * larg
print('Sua parede tem dimensão de {} x {} e sua área é de {}².'.format(larg,alt,área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))