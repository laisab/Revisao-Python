def aumentar(valor, porcentagem):
    """
    Aumenta o valor de acordo com a porcentagem.

    Args:
        valor: valor que deve ser acrescido.
        porcentagem: número da porcentagem para aumentar o valor.

    Return:
        Valor já acrescido pela porcentagem.
    """
    calculo = valor * (1 + (porcentagem / 100))
    return round(calculo, 2)


def diminuir(valor, porcentagem):
    """
    Diminui o valor de acordo com a porcentagem.

    Args:
        valor: valor que deve ser diminuído.
        porcentagem: número da porcentagem para diminuir o valor.

    Return:
        Valor já diminuído pela porcentagem.
    """
    calculo = valor * (1 - (porcentagem / 100))
    return round(calculo, 2)
