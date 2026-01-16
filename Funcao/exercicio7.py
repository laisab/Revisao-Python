"""
Exercício 7: Somador Infinito (*args)
E se quisermos somar 2 números? Ou 5? Ou 50? O *args resolve isso.

1 - Crie uma função chamada somar_tudo que receba o parâmetro especial *args.
2 - Dentro da função, use um loop for (ou a função sum()) para somar todos os números passados.
3 - Retorne o total.
4 - Teste passando 5, 10, 20, 30 de uma vez só.
"""


def somar_tudo(*args):
    return sum(args)


print(somar_tudo(1, 2, 3, 4, 5))
print(somar_tudo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(somar_tudo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
