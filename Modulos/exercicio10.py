"""
Reescreva o código do arquivo cumprimento.py do exercício anterior.

Mantenha a função dar_oi().
Faça com que os print e a chamada da função dar_oi() só sejam executados se o arquivo for rodado diretamente
(como script principal), mas não sejam executados se o arquivo for importado por outro.
"""


def dar_oi():
    print("Oi!")


# O if age como um "segurança".
# Ele diz: "Só execute o que está aqui dentro se este arquivo for o PRINCIPAL".
if __name__ == "__main__":
    print("Módulo carregado com sucesso!")
    dar_oi()
