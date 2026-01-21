"""
1 - Crie uma função chamada gerar_quadrados(n) que use yield.
2 - Ela deve gerar o quadrado dos números de 0 até n.
3 - Crie o objeto gerador para n=5.
4 - Itere sobre esse gerador usando um for e imprima os valores um a um.
"""


def gerar_quadrados(n):
    for numero in range(0, n + 1):
        yield numero ** 2


valores = gerar_quadrados(5)

for valor in valores:
    print(valor)
