"""
1 - Abra o arquivo meu_poema.txt em modo leitura ('r').
2 - Leia o conteúdo e armazene numa variável.
3 - Abra um novo arquivo chamado copia_poema.txt em modo escrita ('w').
4 - Escreva o conteúdo da variável neste novo arquivo.
"""
with open('meu_poema.txt', 'r') as arquivo_leitura:
    conteudo = arquivo_leitura.read()

with open('copia_poema.txt', 'w') as arquivo_escrita:
    arquivo_escrita.write(conteudo)
    