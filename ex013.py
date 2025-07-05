# Desafio 13
"""
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário com 15% de aumento.
"""
salario = float(input('Digite o salário: '))
percentual = float(input('Dgite o percentual de aumento: '))
print(
    f'O salário com aumento de 15% é R$ {salario * (1 + percentual / 100):.2f}.')
