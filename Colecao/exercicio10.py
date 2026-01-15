"""
Exercício 10: Fila de Atendimento (Deque)
Deque é uma lista otimizada para adicionar/remover das pontas.

1 - Crie um deque com os números [1, 2, 3].
2 - Adicione o número 4 no lado direito.
3 - Adicione o número 0 no lado esquerdo.
4 - Remova o elemento da direita e imprima o resultado final do deque.
"""

from collections import deque

lista_numeros = [1, 2, 3]
deq_numeros = deque(lista_numeros)
print(f'Deque original: {deq_numeros}')

deq_numeros.append(4)
deq_numeros.appendleft(0)
print(f'Deque alterado: {deq_numeros}')

deq_numeros.pop()
print(f'Deque alterado: {deq_numeros}')
