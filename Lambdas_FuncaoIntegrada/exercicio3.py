"""
Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
1 - Use filter e uma lambda para criar uma nova lista contendo apenas os números pares.
2 - Imprima a lista filtrada.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

numeros_pares = filter(lambda resultado: resultado % 2 == 0, numeros)
print(list(numeros_pares))
