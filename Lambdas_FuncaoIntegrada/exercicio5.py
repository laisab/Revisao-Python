"""
any: Retorna True se pelo menos um for verdadeiro.
all: Retorna True se todos forem verdadeiros.

Dada a lista de notas: notas = [8.5, 9.0, 7.5, 6.0].
1 - Use all para verificar se todos os alunos tiraram nota maior ou igual a 7 (imprima o resultado).
2 - Use any para verificar se algum aluno tirou nota maior que 9.5 (imprima o resultado).
"""
notas = [8.5, 9.0, 7.5, 6.0]
print(notas)

print(f'Todos os alunos tiraram nota >= 7: {all(nota >= 7 for nota in notas)}')  # False
print(f'Algum aluno tirou nota > 9,5: {any(nota > 9.5 for nota in notas)}')  # False
