"""
Dada a lista de tuplas (Produto, Preço):
produtos = [("Camiseta", 50), ("Calça", 120), ("Meia", 15)].
1 - Use sorted para ordenar a lista do mais barato para o mais caro.
+   Dica: No parâmetro key, use uma lambda que retorne o segundo elemento da tupla (o preço).
2 - Imprima a lista ordenada.
"""
produtos = [("Camiseta", 50), ("Calça", 120), ("Meia", 15)]
print(f'Produtos: {produtos}\n')
print(f'Mais barato ao mais caro:\n{sorted(produtos, key=lambda preco: preco[1])}')
