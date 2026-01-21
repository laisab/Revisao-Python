"""
1 - Importe o reduce do módulo functools.
Dada a lista numeros = [1, 2, 3, 4, 5].
2 - Use reduce com uma lambda para multiplicar todos os números (1 * 2 * 3 * ...).
3 - Imprima o resultado final.
"""

from functools import reduce

numeros = [1, 2, 3, 4, 5]
print(numeros)

multiplicacao = lambda num1, num2: num1 * num2
resultado = reduce(multiplicacao, numeros)
print(resultado)
