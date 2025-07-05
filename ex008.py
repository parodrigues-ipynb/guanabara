# Desafio 8
"""
Escreva um programa que leia um valor em metros e
o exiba convertido em centímetros e milímetros.
"""
num = float(input('Digite o comprimento em metros (m): '))
print(
    f'O valor em centímetros (cm) é {num * 100:.0f}.\nO valor em milímetros é {num * 1000:.0f}.')
