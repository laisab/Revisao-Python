"""
Exercício 2: Dados Geográficos (Tuplas)
Tuplas são imutáveis (não mudam depois de criadas).

1 - Crie uma tupla chamada coordenadas contendo dois números (latitude e longitude).
2 - Tente alterar o primeiro valor da tupla para outro número.
*   Obs: O objetivo é ver o erro acontecer. Comente a linha do erro depois.
3 - Imprima os valores separadamente.
"""
coordenadas = (57, 32)
print(f'Coordenadas: {coordenadas}\n')

"""
coordenadas[0] = 70
print(f'Coordenadas: {coordenadas}')
"""

latitude, longitude = coordenadas
print(f'Latitude: {latitude}\nLongitude: {longitude}')
