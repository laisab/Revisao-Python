"""
Para entrar em um sistema, duas coisas precisam ser verdadeiras ao mesmo tempo.
1 - Defina uma variável como "admin" e senha como "1234".
2 - Crie duas variáveis (coloque os valores que quiser para testar).
3 - Faça um if que verifique se o usuário digitado é igual ao correto e se a senha digitada é igual à correta.
*   Se ambos forem verdadeiros: "Login realizado com sucesso!"
*   Caso contrário: "Usuário ou senha inválidos."
"""
usuario_correto = 'admin'
senha_correta = '1234'
usuario_digitado = input('Digite o usuário: ')
senha_digitada = input('Digite a senha: ')

if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
    print('Login realizado com sucesso!')
else:
    print('Usuário ou senha inválidos!')
