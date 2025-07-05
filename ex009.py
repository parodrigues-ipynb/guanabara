# Desafio 9
"""
Faça um programa que leia um número inteiro qualquer e mostre
na tela sua tabuada.
"""
num = int(input('Digite um número inteiro: '))

# Número de dígitos na variável <num>
dig_num = len(str(abs(num)))
dig_num10 = len(str(abs(num * 10)))
'''
abs() garante que não teremos sinal negativo (-) em números negativos
str() transforma o valor absoluto em string
len() pega o comprimento da string
e.g.: -123
abs() -> 123
str() -> '123'
len() ->  ^^^ comprimento da string = 3 Unicodes
'''

# Variável para tamanho da linha
# número de dígitos do número + ' x __ = ' + (número x 10)
lin = dig_num + 8 + dig_num10

print('-' * lin)
for value in range(1, 11):
    print(f'{num} x {value:2d} = {num * value}')
print('-' * lin)
