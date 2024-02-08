#34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Pra salários superiores a r$ 1.250,00, calcule um aumento de 10%, para inferiores ou iguais o aumento é de 5%

salario = float(input('Digite o salário do seu funcionário: '))
if salario > 1250:
    superior = salario + (salario * 10 / 100)
    print('O salário que era R${:.2f} com novo ajuste de 15% fica R${:.2f}'.format(salario, superior))

elif salario <= 1250:
    inferior = salario + (salario * 5 / 100)
    print('O salário que era {:.2f} com novo ajuste de 5% ficará R${:.2f}'.format(salario, inferior))


