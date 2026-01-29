"""
1 - Crie uma função meu_decorador(funcao_original) que receba uma função.
2 - Dentro, defina uma função wrapper() (envelope).
*   O wrapper deve imprimir "--- Antes ---".
*   Chamar a funcao_original().
*   Imprimir "--- Depois ---".
3 - O decorador deve retornar o wrapper.
4 - Defina uma função simples falar() que imprime "Olá!".
5 - Decore manualmente: falar_decorado = meu_decorador(falar).
6 - Chame falar_decorado().
"""


def meu_decorador(funcao_original):
    def wrapper():
        print("--- Antes ---")
        funcao_original()
        print("--- Depois ---")

    return wrapper


def falar():
    print("Olá!")


falar_decorado = meu_decorador(falar)
falar_decorado()
