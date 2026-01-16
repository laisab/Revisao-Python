"""
Exercício 3: A Diferença do Retorno (return)
Este é um conceito crucial: Imprimir (mostrar na tela) é diferente de Retornar (devolver um valor para o programa).

1 - Crie uma função chamada somar_numeros que receba dois parâmetros: a e b.
2 - A função deve somar os valores e retornar (return) o resultado.
3 - Fora da função, crie uma variável resultado que receba o retorno dessa função.
4 - Imprima a variável resultado.
"""


def somar_numeros(a, b):
    resultado = a + b
    return resultado


num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))
resultado_soma = somar_numeros(num1, num2)
print(f'\n{num1} + {num2} = {resultado_soma}')
