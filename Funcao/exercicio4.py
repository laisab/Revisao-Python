"""
Exercício 4: Calculadora de Área (Lógica + Retorno)

1 - Crie uma função calcular_area_retangulo que receba base e altura.
2 - A função deve calcular a área (base * altura) e retornar esse valor.
3 - Teste a função com valores diferentes (ex: base 10, altura 5) e exiba o resultado.
"""


def calcular_area_retangulo(base, altura):
    return base * altura


base_retangulo = int(input('Base do retângulo = '))
altura_retangulo = int(input('Altura do retângulo = '))
print(f'\nÁrea do retângulo = {calcular_area_retangulo(base_retangulo, altura_retangulo)}')
