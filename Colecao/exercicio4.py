"""
Exercício 4: Varredura de Dicionário (Mapas)

Vamos iterar sobre o dicionário do exercício anterior.
1 - Use um loop para percorrer o dicionário estoque.
2 - Imprima uma frase para cada item: "Produto: [chave] | Quantidade: [valor]".
*   Dica: Use .items() no loop.
"""
estoque = {'caneta': 10, 'caderno': 20}
novo_item = {'borracha': 15}
estoque.update(novo_item)

for produto, quantidade in estoque.items():
    print(f'Produto: {produto} | Quantidade: {quantidade}')
