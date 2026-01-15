"""
Exercício 5: Filtro de Convidados (Conjuntos / Sets)
Sets não aceitam duplicatas e não têm ordem fixa.

1 - Crie uma lista com nomes repetidos.
2 - Converta essa lista para um conjunto (set) para remover as duplicatas e armazene em uma variável.
3 - Verifique se um determinado nome está no conjunto (use o operador in) e imprima o resultado.
4 - Imprima o conjunto limpo.
"""
nomes = ['Lais', 'Ana', 'Maria', 'Ana', 'Carlos']
conjunto_nomes = set(nomes)
print(f'Lista de nomes: {nomes}\n')

verifica_nome = input('Digite um nome para verificar a existência no conjunto: ')

if verifica_nome in conjunto_nomes:
    print(f'{verifica_nome} está no conjunto.\n')
else:
    print(f'{verifica_nome} não está no conjunto.\n')

print(f'Conjunto de nomes: {conjunto_nomes}')
