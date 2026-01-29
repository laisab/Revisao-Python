"""
1 - Crie um decorador maiusculo.
2 - O wrapper deve chamar a função original, pegar o resultado (string) e retornar esse resultado .upper().
3 - Aplique em uma função retornar_texto() que devolve "olá mundo".
4 - Chame a função e verifique se saiu "OLÁ MUNDO".
"""


def maiusculo(funcao_original):
    def wrapper():
        return funcao_original().upper()
    return wrapper


@maiusculo
def retornar_texto():
    return "olá mundo"


print(retornar_texto())
