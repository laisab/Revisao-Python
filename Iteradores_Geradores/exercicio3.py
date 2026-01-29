"""
1 - Crie uma função contador_regressivo(n) que receba um número.
2 - Use um loop while n > 0.
3 - Use yield n para devolver o número atual.
4 - Decremente n.
5 - Teste a função: for numero in contador_regressivo(5): print(numero).
"""


def contador_regressivo(n):
    while n > 0:
        yield n
        n -= 1


for numero in contador_regressivo(5):
    print(numero)
