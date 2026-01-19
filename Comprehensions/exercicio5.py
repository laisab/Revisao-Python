"""
Set Comprehension é ótimo para matemática e unicidade.

Dada a lista com repetidos: numeros = [10, 15, 20, 25, 30, 35, 40, 10, 20].
1 - Use Set Comprehension (usa chaves {}, mas sem os dois pontos :) para criar um conjunto
contendo o resto da divisão por 3 de cada número.
2 - Imprima o resultado. Observe que, como é um conjunto, os resultados repetidos sumirão automaticamente.
"""
numeros = [10, 15, 20, 25, 30, 35, 40, 10, 20]
print(numeros)

novo_set = {resultado % 3 for resultado in numeros}
print(novo_set)
