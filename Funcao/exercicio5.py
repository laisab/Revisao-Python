"""
Exercício 5: O Valor Padrão (Default Parameters)
Às vezes, queremos que um parâmetro seja opcional.

1 - Crie uma função chamada potencia que receba dois parâmetros: numero e expoente.
2 - Defina o valor padrão do expoente como 2.
3 - A função deve retornar o numero elevado ao expoente.
4 - Teste chamando a função de duas formas:
*   Passando os dois números (ex: 3 e 3 -> deve dar 27).
*   Passando apenas o primeiro número (ex: 4 -> deve dar 16, pois usará o padrão 2).
"""


def potencia(numero, expoente=2):
    resultado = numero ** expoente
    return resultado


res1 = potencia(3, 3)
print(f'Potência = {res1}\n')

res2 = potencia(4)
print(f'Potência = {res2}')
