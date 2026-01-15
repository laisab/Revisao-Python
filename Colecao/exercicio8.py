"""
Exercício 8: Ordem de Chegada (OrderedDict)
Embora dicionários comuns hoje em dia mantenham ordem, o OrderedDict tem métodos especiais de reordenação.

1 - Crie um OrderedDict com três pares: ('A', 1), ('B', 2), ('C', 3).
2 - Mova a chave 'A' para o final do dicionário.
3 - Imprima o dicionário para ver a nova ordem.
"""

from collections import OrderedDict

dicionario = OrderedDict({'A': 1, 'B': 2, 'C': 3})
print(f'Ordem original do dicionário:\n {dicionario}\n')

dicionario.move_to_end('A')
print(f'Nova ordem do dicionário:\n {dicionario}')
