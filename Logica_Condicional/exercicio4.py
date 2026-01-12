"""
No cinema, paga meia-entrada quem é estudante OU quem é idoso (60 anos ou mais).

1 - Crie uma variável para idade e uma variável booleana para posse de carteirinha.
2 - Crie uma estrutura condicional:
*   Se a pessoa tiver idade maior ou igual a 60 OU possuir carteirinha, imprima: "Direito a meia-entrada."
*   Caso contrário, imprima: "Pagamento integral."
"""

idade = int(input('Digite a sua idade: '))
carteirinha = int(input('Possui carteirinha?\n 1 - Sim   2 - Não\n'))

if carteirinha == 1:
    possui_carteirinha = True
else:
    possui_carteirinha = False

if idade >= 60 or possui_carteirinha:
    print('Direito a meia-entrada.')
else:
    print('Pagamento integral.')
