# Desafio 11
"""
Faça um programa que leia a largura e altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2m².
"""
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
ar = l * a
print(
    f'A área da parede é {ar}. É(são) necessário(s) {ar / 2} litro(s) de tinta.')
