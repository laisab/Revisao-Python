"""
1 - Pegue o arquivo teste_novo.txt (do exercício anterior).
2 - Mova-o para dentro da pasta arquivos_temporarios (criada no exercício 6).
*   Dica: O destino deve ser algo como: os.path.join('arquivos_temporarios', 'teste_novo.txt').
"""
import os

caminho_origem = os.path.join(os.getcwd(), 'teste_novo.txt')
print(f'Diretório atual: {os.getcwd()}')
print(f'Arquivos e pastas neste diretório: {os.listdir()}')

try:
    caminho_destino = os.path.join('arquivos_temporarios', 'teste_novo.txt')
    os.rename(caminho_origem, caminho_destino)

    os.chdir('arquivos_temporarios')
    print(f'\nDiretório atual: {os.getcwd()}')
    print(f'Arquivos e pastas neste diretório: {os.listdir()}')
except FileExistsError:
    print('\nNão foi possível renomear o arquivo.')
