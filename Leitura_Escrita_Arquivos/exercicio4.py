"""
1 - Abra o arquivo lista_frutas.txt para leitura.
2 - Leia o arquivo todo com .read() e imprima.
3 - Tente ler novamente com .read() e imprima (deve sair vazio).
4 - Use o comando .seek(0) para voltar o cursor para o início.
5 - Leia e imprima novamente (agora deve funcionar).
"""
with open('lista_frutas.txt', 'r') as arquivo:
    print('\tPrimeira tentativa')
    print(arquivo.read())
    print('\n\tSegunda tentativa')
    print(arquivo.read())

    arquivo.seek(0)
    print('\n\tTerceira tentativa')
    print(arquivo.read())
