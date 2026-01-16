"""
Exercício 9: Lista como Parâmetro

1 - Crie uma função dobrar_lista que receba uma lista de números.
2 - A função deve criar uma nova lista onde cada elemento é o dobro do original.
3 - Retorne essa nova lista.
*   Teste com [1, 2, 3, 4].
"""


def dobrar_lista(lista_numeros):
    nova_lista = [numero * 2 for numero in lista_numeros]
    return nova_lista


lista_dobro = dobrar_lista([1, 2, 3, 4])
print(lista_dobro)
