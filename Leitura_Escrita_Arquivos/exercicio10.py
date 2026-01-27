"""
1 - Remova o arquivo copia_poema.txt usando os.remove.
2 - Remova o arquivo que está dentro da pasta (arquivos_temporarios/teste_novo.txt).
3 - Remova a pasta arquivos_temporarios usando os.rmdir (ela precisa estar vazia para isso funcionar).
"""
import os

print("Removendo o arquivo 'copia_poema.txt'...")
os.remove('copia_poema.txt')
print('Arquivo removido com sucesso!')
print()

print("Removendo o arquivo da pasta temporária...")
os.remove('arquivos_temporarios/teste_novo.txt')
print('Arquivo removido com sucesso!')
print()

print("Removendo a pasta temporária...")
os.rmdir('arquivos_temporarios')
print('Pasta removida com sucesso!')
