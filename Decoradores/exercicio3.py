"""
1 - Use o mesmo código do meu_decorador do exercício anterior.
2 - Crie uma nova função avisar() que imprime "Estou avisando!".
3 - Coloque @meu_decorador em cima da definição de avisar.
4 - Chame avisar() diretamente e veja os prints de "Antes" e "Depois" aparecerem.
"""


def meu_decorador(funcao_original):
    def wrapper():
        print("--- Antes ---")
        funcao_original()
        print("--- Depois ---")

    return wrapper


@meu_decorador
def avisar():
    print("Estou avisando!")


avisar()
