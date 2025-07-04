# Desafio 002
"""
Crie um programa no qual o usuário insira seu nome e seja
impresso na tela 'É um prazer te conhecer, <nome do usuário>!'.
"""

# Solução
nome = input("Insira o seu nome: ")
print("É um prazer te conhecer, " + nome + "\n")

# Solução extra porque fiquei entediado
num1 = input("Insina um número para eu ver o que acontece: ")
num2 = input("Insere outro número aí: ")
num = num1 + num2
print("Número 1 (" + num1 + ") + número 2 (" + num2 + ") = " + num + "\n")
print("Os números são concatenados ao invés de serem algebricamente somados.")
print("A função input() retorna o conteúdo digito com o tipo str.")
print("type(num1) = ", type(num1))
print("type(num2) = ", type(num2))