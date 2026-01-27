"""
1 - Use o comando with open(...) para criar um arquivo chamado meu_poema.txt.
2 - Use o modo 'w' (write).
3 - Escreva uma frase nele (ex: "Batatinha quando nasce...").
4 - Logo em seguida (em outro bloco with), abra o mesmo arquivo no modo 'r' (read), leia o conteúdo e
imprima no console.
"""
with open('meu_poema.txt', 'w') as arquivo:
    arquivo.write("Batatinha quando nasce...")

with open('meu_poema.txt', 'r') as arquivo:
    print(arquivo.read())
