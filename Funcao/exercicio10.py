"""
Exercício 10: O Mestre das Funções (Combinação)

1 - Crie uma função chamada analisar_notas.
2 - Ela deve aceitar vários números (notas) usando *args.
3 - Ela deve aceitar um parâmetro opcional situacao=False (Default parameter).
4 - A função deve calcular a média das notas.
5 - Ela deve retornar um dicionário com:
*   "total_notas": quantidade de notas passadas.
*   "maior_nota": a maior nota.
*   "media": a média calculada.
6 - Se situacao for True, adicione também ao dicionário a chave "status":
*   "Aprovado" se média >= 7.
*   "Reprovado" se média < 7.
"""


def analisar_notas(*args, situacao=False):
    media_notas = sum(args) / len(args)

    dict_aluno = {'Total de Notas': len(args), 'Maior Nota': max(args), 'Média': media_notas}

    if situacao:
        if media_notas >= 7:
            dict_aluno['Status'] = 'Aprovado'
        else:
            dict_aluno['Status'] = 'Reprovado'

    return dict_aluno


aluno1 = analisar_notas(5, 7, 5, 2, situacao=True)
for chave, valor in aluno1.items():
    print(f'{chave}: {valor}')

print()

aluno2 = analisar_notas(5, 7, 3, 0)
for chave, valor in aluno2.items():
    print(f'{chave}: {valor}')
