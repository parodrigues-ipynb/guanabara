# Desafio 10
"""
Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos dólares ela pode comprar.

Considere US$ 1.00 = R$ 3.27
"""
carteira = float(input('Digite o valor na sua carteira: '))
print(f'Você pode comprar US$ {carteira / 3.27:.2f}.')
