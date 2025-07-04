# Desafio 003
"""
Crie um programa que leia dois números e mostre a soma entre eles.
"""
try:
    num_1 = float(input('Digite um número: ').replace(',', '.'))
    num_2 = float(input('Digite outro número: ').replace(',', '.'))
    # Converter já na atribuição o valor diminui as chances de erro, pois
    # num_1 = input()
    # num_1 = float(num_1)
    # faz com que tenha duas chances de algo dar errado na execução.
    #
    # .replace(',', '.') é uma boa prática para usuários em que a notação
    # numérica seja 3,14 ao invés de 3.14, que é a forma como o Python
    # entende valores numéricos Reais.
    soma = num_1 + num_2
    print(f'{num_1} + {num_2} = {soma}')
except ValueError:
    print('''Por favor, digite apenas valores numéricos válidos!
          
Exemplos de valores válidos:
1, 2, 3, 4, 5...
1.5, 3.14, 5.99999...''')
