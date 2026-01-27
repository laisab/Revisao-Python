"""
1 - Defina uma variável nome_pasta = "arquivos_temporarios".
2 - Use os.path.join para criar o caminho completo (diretório atual + nome da pasta).
3 - Use os.mkdir para criar essa pasta no seu computador.
*   Dica: Se rodar duas vezes, vai dar erro porque a pasta já existe.
Tente tratar isso com try/except FileExistsError ou verificando com os.path.exists.
"""
import os

nome_pasta = "arquivos_temporarios"

try:
    os.mkdir(os.path.join(os.getcwd(), nome_pasta))
except FileExistsError:
    print('Não foi possível criar a pasta porque ela já existe.')
