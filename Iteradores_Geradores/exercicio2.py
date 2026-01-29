"""
Dada a string palavra = "Python".
1 - Crie um iterador dela (iter(palavra)).
2 - Crie um loop while True.
3 - Dentro dele, use try/except StopIteration.
4 - No try, imprima o next() do iterador.
5 - No except, use break para sair do loop.
"""
palavra = "Python"
iterador = iter(palavra)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
