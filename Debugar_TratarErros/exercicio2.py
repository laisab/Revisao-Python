"""
1 - Crie uma função cadastrar_usuario(idade).
2 - Se a idade for menor que 0 ou maior que 120, use o comando
raise ValueError("Idade inválida: deve estar entre 0 e 120").
3 - Fora da função, chame cadastrar_usuario(150) dentro de um bloco try/except para capturar essa mensagem
e imprimi-la amigavelmente.
"""


def cadastrar_usuario(idade):
    if idade < 0 or idade > 120:
        raise ValueError("Idade inválida: deve estar entre 0 e 120.")


try:
    cadastrar_usuario(150)
except ValueError as e:
    print(e)
