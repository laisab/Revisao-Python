"""
1 - Use a mesma lista de produtos do exercício anterior.
2 - Use a função max com uma lambda no parâmetro key para encontrar a tupla do produto mais caro.
3 - Use a função min com key para encontrar o mais barato.
4 - Imprima os dois produtos encontrados.
"""
produtos = [("Camiseta", 50), ("Calça", 120), ("Meia", 15)]
print(f'Produtos: {produtos}\n')

produto_caro = max(produtos, key=lambda preco: preco[1])
produto_barato = min(produtos, key=lambda preco: preco[1])

print(f'Produto mais caro: {produto_caro}\nProduto mais barato: {produto_barato}')
