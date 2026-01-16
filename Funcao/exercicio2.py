"""
Exercício 2: Personalizando (def com parâmetro)
Funções ficam úteis quando aceitam dados externos.

1 - Crie uma função chamada saudar_usuario que receba um parâmetro nome.
2 - A função deve imprimir: "Olá, [nome]! Tudo bem?".
3 - Chame a função passando o seu nome.
"""


def saudar_usuario(nome):
    print(f'Olá, {nome}! Tudo bem?')


nome_usuario = input('Qual é o seu nome? ')
saudar_usuario(nome_usuario)
