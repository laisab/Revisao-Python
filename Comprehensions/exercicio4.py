"""
Comprehensions também funcionam com chaves {} para criar dicionários.

Dado o dicionário: precos = {'Notebook': 3000, 'Mouse': 50, 'Teclado': 150}.
1 - Use Dict Comprehension para criar um novo dicionário onde você aplica um desconto de 10% em todos os valores.
2 - Além disso, filtre para manter no novo dicionário apenas os produtos que, após o desconto, custem mais de 100 reais.
"""
precos = {'Notebook': 3000, 'Mouse': 50, 'Teclado': 150}
desconto = 0.9
precos_desconto = {chave: valor * 0.9 for chave, valor in precos.items() if (valor * 0.9) > 100}
print(precos_desconto)
