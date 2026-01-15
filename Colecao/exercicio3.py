"""
Exercício 3: O Estoque da Loja (Dicionários)
Dicionários mapeiam chaves (únicas) para valores.

1 - Crie um dicionário onde a chave é o nome do produto e o valor é a quantidade. Ex: {"caneta": 10, "caderno": 5}.
2 - Acesse e imprima a quantidade de "caneta".
3 - Altere a quantidade de "caderno" para 20.
4 - Adicione um novo item: "borracha" com quantidade 15.
"""
estoque = {'caneta': 10, 'caderno': 5}

print(f'Quantidade de caneta: {estoque.get('caneta')}')

estoque['caderno'] = 20
print(f'Quantidade de caderno: {estoque.get('caderno')}')

novo_item = {'borracha': 15}
estoque.update(novo_item)
print(f'Quantidade de borracha: {estoque.get('borracha')}')
