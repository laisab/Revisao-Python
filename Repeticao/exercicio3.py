"""
Vamos automatizar a matemática básica.

1 - Defina uma variável com um valor.
2 - Dentro do loop, imprima a tabuada desse número até o 10.
"""
valor = int(input('Escolha um número: '))

for numero in range(0, 11):
    print(f'{valor} * {numero} = {valor*numero}')
