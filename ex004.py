# Desafio 004
"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele.
"""
something = input('Digite algo: ')
print(f'''
Sua entrada foi {something}
O tipo desta entrada é {type(something)}

RELATÓRIO DOS CARACTERES INSERIDOS
A entrada é do tipo alfanumérico?
.isalnum(): {something.isalnum()}

A entrada é do tipo alfabético?
.isalpha(): {something.isalpha()}

A entrada do tipo dígito?
.isdigit(): {something.isdigit()}

A entrada é do tipo numérico?
.isnumeric(): {something.isnumeric()}

A entrada é do tipo decimal?
.isdecimal(): {something.isdecimal()}

Os caracteres alfabéticos da entrada são todos minúsculos?
.islower(): {something.islower()}

Os caracteres alfabéticos da entrada são todos maiúsculos?
.isupper(): {something.isupper()}

Os caracteres inseridos são todos 'espaço'?
.isspace(): {something.isspace()}

Os caracteres inseridos são imprimíveis?
.isprintable(): {something.isprintable()}
''')
