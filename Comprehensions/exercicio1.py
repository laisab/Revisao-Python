"""
Vamos começar combinando lógica matemática com compreensão de lista.

1 - Crie uma lista com números de 0 a 20 usando range().
2 - Use uma List Comprehension para gerar uma nova lista chamada quadrados_pares.
3 - Essa nova lista deve conter o quadrado apenas dos números que forem pares.
4 - Imprima a lista final.
"""
lista_numeros = [numero for numero in range(0, 21)]
print(lista_numeros)

quadrados_pares = [numero*numero for numero in lista_numeros if numero % 2 == 0]
print(quadrados_pares)
