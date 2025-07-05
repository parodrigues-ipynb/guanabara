# Desafio 15
"""
Escreva um programa que pergunte a quantidade de km percorridos por
um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar sabendo que o aluguel custa R$ 60,00 por dia
e R$ 0,15 por km rodado.
"""
km = float(input('Quantos km foram rodados? '))
dias = int(input('Por quantos dias o carro permaneceu alugado? '))
print(f'O valor a pagar é R$ {(km * 0.15 + dias * 60):.2f}.')
