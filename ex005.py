# Notas pessoais
"""
Ordem de precedência para operadores aritméticos no Python:
()
**
* / // %
+ -

Quando utilizamos funções internas como pow() ao invés de **,
perdemos a ordem de precedência.
"""

# Desafio 5
"""
Faça um programa que leia um número inteiro e mostre na tela seu
sucessor e seu antecessor.
"""
num = int(input('Digite um número inteiro: '))
print(f'Antecessor: {num - 1}, número: {num}, sucessor: {num + 1}')
