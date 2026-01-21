"""
Dada a lista de preços em dólares: precos_dolar = [100, 50, 250].
1 - Use map junto com uma lambda para converter esses valores para reais (considere 1 dólar = 5.50 reais).
2 - Converta o resultado do map para uma lista (list()) e imprima.
"""
precos_dolar = [100, 50, 250]
print(f'Preços em dólares: {precos_dolar}')

print(f'Preços convertidos em reais: {list(map(lambda preco: preco * 5.50, precos_dolar))}')
