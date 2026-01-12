"""
Muitos programas rodam infinitamente até que o usuário peça para sair. Vamos criar um.

1 - Crie um loop infinito.
2 - Dentro do loop, peça para o usuário digitar algo.
3 - Se o usuário digitar a palavra "sair":
*   Imprima "Encerrando o programa..."
4 - Caso contrário, apenas imprima o que o usuário digitou e deixe o loop rodar novamente.
"""
while True:
    entrada_usuario = input('Digite algo: ')

    if entrada_usuario == 'sair':
        print('Encerrando o programa...')
        break
    else:
        print(f'{entrada_usuario}\n')
