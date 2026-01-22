"""
O código abaixo está cheio de problemas potenciais.

def pegar_elemento(lista, indice):
    return lista[indice]

minha_lista = ["A", "B", "C"]
print(pegar_elemento(minha_lista, 5))

1 - Reescreva a função pegar_elemento adicionando um tratamento de erro (try/except).
2 - Se o índice for inválido (IndexError) ou se o índice não for um número inteiro (TypeError),
a função deve retornar a string "Índice inválido".
3 - Teste chamando com índice 5 e depois com índice "a".
"""


def pegar_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Índice inválido"
    except TypeError:
        return "Índice inválido"
    # except (IndexError, TypeError):
    #     return "Índice inválido"


minha_lista = ["A", "B", "C"]
print(pegar_elemento(minha_lista, 1))
print(pegar_elemento(minha_lista, 5))
print(pegar_elemento(minha_lista, "a"))
