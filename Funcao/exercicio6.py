"""
Exercício 6: Documentando seu Código (Docstrings)
Boas práticas importam!

1 - Crie uma função chamada verificar_par que recebe um número n.
2 - A função deve retornar True se for par e False se for ímpar.
3 - Obrigatório: Adicione uma Docstring (logo abaixo do def, entre três aspas) explicando:
*   O que a função faz.
*   O que é o parâmetro n.
*   O que ela retorna.
4 - No final, use o comando help(verificar_par) para ver sua documentação impressa no console.
"""


def verificar_par(n):
    """
    Verifica se um número é par ou não.

    Args:
        n (int): número para verificação.

    Returns:
        True/False (bool): True para par; False para ímpar.
    """
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número inteiro: '))
par = verificar_par(num)
print(f'{num} é par? R.: {par}\n')
print(help(verificar_par))
