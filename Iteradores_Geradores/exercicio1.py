"""
1 - Crie uma lista simples: nomes = ["Ana", "Bia", "Caio"].
2 - Transforme essa lista (Iterável) em um Iterador usando a função iter().
3 - Use a função next() três vezes para imprimir cada nome manualmente.
4 - Use next() uma quarta vez dentro de um bloco try/except para capturar o erro StopIteration.
"""
nomes = ["Ana", "Bia", "Caio"]
iterador = iter(nomes)

print(next(iterador))
print(next(iterador))
print(next(iterador))

try:
    print(next(iterador))
except StopIteration as e:
    print(e)
