"""
Dada a lista de variações de temperatura: variacoes = [-1.5, 2.2, -3.8, 0.5].
1 - Use map e abs para criar uma lista com os valores absolutos (todos positivos).
2 - Use sum e len para calcular a média desses valores absolutos.
3 - Use round para arredondar a média final para 2 casas decimais e imprima.

def mapear_valores_absolutos(variacao):
    valores_absolutos = []

    for valor in variacao:
        valores_absolutos.append(abs(valor))

    return valores_absolutos


variacoes_absolutas = mapear_valores_absolutos(variacoes)
"""
variacoes = [-1.5, 2.2, -3.8, 0.5, 3.8]
print(f'Variações de temperatura: {variacoes}')

variacoes_absolutas = list(map(abs, variacoes))
media_absolutas = sum(variacoes_absolutas) / len(variacoes_absolutas)
media_final = round(media_absolutas, 2)

print(f'Valores absolutos de temperatura: {variacoes_absolutas}\nMédia das temperaturas: {media_final}')
