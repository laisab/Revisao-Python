"""
Exercício 6: Contador de Letras (Counter)
O Counter conta automaticamente a frequência de itens.

1 - Crie uma string longa, ex: texto = "abacate e banana".
2 - Use Counter(texto) para contar as letras.
3 - Imprima quantas vezes a letra "a" aparece.
4 - Imprima as 2 letras mais comuns.
"""

from collections import Counter

texto = "Lais Aparecida Borges"
print(f'Quantidade de letras:\n {Counter(texto)}\n')

# letra_a = Counter(texto)
# print(f'Quantidade de letras "a":\n {letra_a['a']}')
print(f'Quantidade de letras "a":\n {Counter(texto)['a']}\n')
print(f'2 letras mais comuns:\n {Counter(texto).most_common(2)}')
