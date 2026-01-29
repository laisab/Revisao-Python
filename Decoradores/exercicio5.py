"""
1 - Crie um decorador medir_tempo.
2 - O wrapper deve aceitar *args e **kwargs.
3 - O wrapper deve imprimir "Chamando função...".
4 - O wrapper deve chamar a função original passando *args e **kwargs e guardar o resultado.
5 - O wrapper deve imprimir "Função finalizada." e retornar o resultado.
6 - Aplique na função soma(a, b) e teste soma(10, 20).
"""


def medir_tempo(funcao):
    def wrapper(*args, **kwargs):
        print("Chamando função...")
        resultado = funcao(*args, **kwargs)
        print("Função finalizada.\n")
        return resultado
    return wrapper


@medir_tempo
def soma(a, b):
    return a + b


print(soma(10, 20))
