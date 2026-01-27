"""
1 - Abra o arquivo meu_poema.txt criado anteriormente no modo 'w' e escreva "Esqueci o poema.".
2 - Feche o arquivo.
3 - Agora, abra no modo 'a' (append) e escreva "\nMas agora lembrei.".
4 - Abra para leitura ('r'), leia tudo e imprima.
*   Objetivo: Perceber que o passo 1 apagou o "Batatinha..." original, mas o passo 3 manteve o texto do passo 1.
"""
with open('meu_poema.txt', 'w') as arquivo:
    arquivo.write("Esqueci o poema.")

with open('meu_poema.txt', 'a') as arquivo:
    arquivo.write("\nMas agora lembrei.")

with open('meu_poema.txt', 'r') as arquivo:
    print(arquivo.read())
