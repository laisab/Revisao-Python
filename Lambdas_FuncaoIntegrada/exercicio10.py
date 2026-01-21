"""
Lista 1: nomes = ["Ana", "Bruno", "Carla"].
Lista 2: idades = [25, 30, 22].
1 - Use zip para criar uma lista de tuplas (Nome, Idade).
2 - Converta o resultado do zip também para um dicionário (dict()) e imprima ambos.
"""
nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]
print(f'Nomes: {nomes}\nIdades: {idades}')

dados = zip(nomes, idades)
print(list(dados))

final = dict(zip(nomes, idades))
print(final)
