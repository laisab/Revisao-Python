"""
Exercício 7: Agrupando Nomes (DefaultDict)
O defaultdict evita erros quando buscamos uma chave que não existe, criando um valor padrão.

1 - Crie um defaultdict onde o valor padrão seja uma lista (list).
2 - Dada a lista nomes = ["Ana", "Antonio", "Beatriz", "Breno", "Carlos"]:
*   Faça um loop para agrupar os nomes pela primeira letra.
    Ex: meu_dict['A'].append('Ana').
3 - Imprima o dicionário final. Espera-se algo como: {'A': ['Ana', 'Antonio'], 'B': ['Beatriz', ...], ...}.
"""

from collections import defaultdict

dicionario = defaultdict(list)
lista_nomes = [('A', 'Ana'), ('A', 'Antonio'), ('B', 'Beatriz'), ('B', 'Breno'), ('C', 'Carlos'), ('B', 'Brenda')]

for letra, nome in lista_nomes:
    dicionario[letra].append(nome)

print(dicionario)

"""
nomes = ["Ana", "Antonio", "Beatriz", "Breno", "Carlos"]
dicionario = defaultdict(list)

for nome in nomes:
    primeira_letra = nome[0]  # Pega a primeira letra da string
    dicionario[primeira_letra].append(nome)
"""
