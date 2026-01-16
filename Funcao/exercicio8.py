"""
Exercício 8: Montador de Perfil (**kwargs)
O **kwargs permite passar argumentos nomeados sem limite, criando um dicionário interno.

1 - Crie uma função criar_perfil que receba o parâmetro **kwargs.
2 - A função deve percorrer os itens recebidos (chave e valor) e imprimir: "Característica [chave]: [valor]".
3 - Chame a função passando dados variados, ex: nome="Ana", idade=25, cidade="São Paulo".
"""


def criar_perfil(**kwargs):
    for chave, valor in kwargs.items():
        print(f'Característica {chave}: {valor}')
    print()


criar_perfil(nome='Ana', idade=25, cidade='São Paulo')
criar_perfil(nome='Lais', idade=22, cidade='Itapecerica da Serra')

nome_usuario = input('Digite seu nome: ')
idade_usuario = int(input('Digite sua idade: '))
cidade_usuario = input('Digite a cidade em que mora: ')
print()

criar_perfil(nome=nome_usuario, idade=idade_usuario, cidade=cidade_usuario)
