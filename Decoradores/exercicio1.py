"""
1 - Crie uma função criar_saudacao(saudacao).
2 - Dentro dela, defina uma função interna saudar(nome) que imprime f"{saudacao}, {nome}!".
3 - A função externa deve retornar a função interna (sem parênteses).
4 - Crie uma variável bom_dia = criar_saudacao("Bom dia").
5 - Agora chame bom_dia("Maria").
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        print(f"{saudacao}, {nome}!")

    return saudar


bom_dia = criar_saudacao("Bom dia")
bom_dia("Maria")
