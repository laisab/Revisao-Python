"""
Vamos trabalhar com textos.

1 - Crie uma variável com o seu primeiro nome.
2 - Crie uma variável com o seu sobrenome.
3 - Crie uma terceira variável que seja a concatenação (junção) das duas anteriores, com um espaço entre elas.
4 - Imprima a terceira variável e, em seguida, imprima o tamanho desse texto (número de caracteres).
"""

primeiro_nome = 'Lais'
segundo_nome = 'Aparecida'  # Verificação de um tamanho diferente
sobrenome = 'Borges'
nome_completo = primeiro_nome + ' ' + segundo_nome + ' ' + sobrenome

print(f'Nome completo: {nome_completo}')
print(f'Seu nome tem {len(nome_completo)} caracteres.')
