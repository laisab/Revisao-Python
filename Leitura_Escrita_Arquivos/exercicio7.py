"""
1 - Crie um arquivo vazio chamado teste_velho.txt.
2 - Verifique se ele existe na pasta (pode usar os.listdir para confirmar visualmente ou os.path.exists).
3 - Use os.rename para mudar o nome dele para teste_novo.txt.
"""
import os

nome_arquivo = "teste_velho.txt"

with open(nome_arquivo, 'w') as arquivo:
    print('Arquivo criado')

    if os.path.exists(nome_arquivo):
        print('\nO arquivo existe.')

        try:
            os.rename(nome_arquivo, "teste_novo.txt")
            print('\nArquivo renomeado.')
        except OSError as e:
            print(f'\nNão foi possível renomear o arquivo: {e}')
    else:
        print('\nO arquivo não existe.')
