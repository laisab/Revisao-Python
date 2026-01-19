"""
Vamos processar uma frase inteira em uma linha.

Dada a frase: "O Python é uma linguagem de programação poderosa e divertida".
1 - Primeiro, divida a frase em uma lista de palavras usando .split().
2 - Use List Comprehension para criar uma lista contendo apenas as palavras que tenham mais de 4 letras.
3 - Além de filtrar, converta essas palavras para maiúsculas (.upper()) na mesma expressão.
"""
frase = "O Python é uma linguagem de programação poderosa e divertida"
lista_palavras = frase.split()

palavras_quatro_letras = [palavra.upper() for palavra in lista_palavras if len(palavra) > 4]
print(palavras_quatro_letras)
