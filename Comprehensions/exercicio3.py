"""
Este é um clássico. Às vezes recebemos uma "lista de listas" (matriz) e queremos uma lista simples.

Dada a matriz: matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
1 - Use uma List Comprehension com dois for internos para "achatar" (flatten) essa matriz.
2 - O resultado deve ser uma lista única: [1, 2, 3, 4, 5, 6, 7, 8, 9].
*   Dica: A ordem de leitura é: "Para cada linha na matriz, para cada item na linha..."
"""
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)

lista_unica = [item for linha in matriz for item in linha]
print(lista_unica)
