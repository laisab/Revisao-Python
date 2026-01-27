"""
1 - Crie um arquivo lista_frutas.txt e escreva nele:
Maçã
Banana
Uva

2 - Abra o arquivo para leitura.
3 - Use o método .readline() (no singular) duas vezes e imprima o resultado de cada uma.
4 - Depois, use .readlines() (no plural) para pegar o restante e imprima.
"""
with open('lista_frutas.txt', 'w') as arquivo:
    arquivo.write('Maca\n')
    arquivo.write('Banana\n')
    arquivo.write('Uva')

with open('lista_frutas.txt', 'r') as arquivo:
    print(arquivo.readline())
    print()
    print(arquivo.readlines())
