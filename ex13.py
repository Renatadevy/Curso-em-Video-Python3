#13 Crie um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Qual salário do funcionário R$: '))
novo = salario + (salario * 15 /100)
print('O salário que era R$ {:.2f} com novo ajuste de 15% fica R$ {:.2f}'.format(salario, novo))

