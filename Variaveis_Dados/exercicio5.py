"""
Para este exercício, copie e complete o código fornecido no seu editor para entender onde as variáveis "vivem".

Tarefa: Defina o x local como 5, rode o código e observe se o último print exibe 5 ou 10.
Isso demonstrará a diferença entre escopos.
"""
x = 10  # Variável Global


def minha_funcao():
    x = 5
    print("Valor de x dentro da função:", x)


minha_funcao()
print("Valor de x fora da função:", x)
