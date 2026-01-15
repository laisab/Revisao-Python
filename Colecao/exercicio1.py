"""
Exercício 1: Gerenciador de Tarefas (Listas)
Listas são mutáveis e ordenadas.

1 - Crie uma lista chamada tarefas com 3 strings.
2 - Adicione uma nova tarefa no final.
3 - Remova uma tarefa que não seja a primeira nem a última.
4 - Imprima a primeira tarefa da lista e a lista atualizada completa.
"""
tarefas = ['Estudar Python', 'Fazer compras', 'Lavar o carro']
print(tarefas)

tarefas.append('Ler um livro')
print(tarefas)

tarefas.remove('Fazer compras')

print(f'\nPrimeira tarefa da lista: {tarefas[0]}\n')
print(f'Lista completa: {tarefas}')
