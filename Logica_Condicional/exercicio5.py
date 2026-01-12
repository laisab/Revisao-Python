"""
O operador is verifica a identidade do objeto, ou seja, se eles são o mesmo objeto na memória.
Ele é muito usado para verificar se uma variável é "vazia" (None).
1 - Crie uma variável chamada resposta_servidor e atribua a ela o valor especial None
(isso significa que o servidor ainda não respondeu ou deu erro).
2 - Faça um teste lógico usando is:
*   Se resposta_servidor for (is) None, imprima: "Aguardando resposta..."
*   Caso contrário, imprima: "Resposta recebida!"
3 - Depois, faça um segundo teste usando is not:
*   Se resposta_servidor não for (is not) None, imprima: "Processando dados..."
"""
resposta_servidor = None

if resposta_servidor is None:
    print('Aguardando resposta...')
else:
    print('Resposta recebida!')

if resposta_servidor is not None:
    print('Processando dados...')
