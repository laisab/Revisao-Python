"""
Crie um programa que represente os dados de um produto em uma loja. Você deve declarar três variáveis:

1 - Uma variável para o nome do produto (String).
2 - Uma variável para a quantidade comprada (Int).
3 - Uma variável para o preço unitário (Float).

Tarefa: Exiba no console uma frase que utilize essas variáveis.
Em seguida, mostre o tipo de dado da variável do preço.
"""

nome_produto = "laranja"
qtde_comprada = 5
preco_unitario = 0.73

print(f"Você comprou {qtde_comprada} {nome_produto}(s) cujo preço unitário é R${preco_unitario}\n")
print("TIPOS DAS VARIÁVEIS")
print(f"Nome do produto: {type(nome_produto)}")
print(f"Quantidade comprada: {type(qtde_comprada)}")
print(f"Preço unitário: {type(preco_unitario)}")
