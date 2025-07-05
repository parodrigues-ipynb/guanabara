# Desafio 12
"""
Faça um algoritmo que leia o preço de um produto e mostre
seu novo preço com 5% de desconto.
"""
preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o percentual de desconto: '))
print(f'O preço com 5% de desconto é R$ {preco * (1 - desconto / 100):.2f}.')
