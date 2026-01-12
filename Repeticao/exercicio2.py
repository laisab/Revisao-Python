"""
A função range(inicio, fim, passo) é muito poderosa para gerar sequências numéricas.

Escreva um programa que use um loop for e o range.
O objetivo é imprimir todos os números pares de 0 até 20 (incluindo o 20).

Dica: Lembre-se que o parâmetro "fim" do range é exclusivo (ele para antes),
então ajuste o valor final para garantir que o 20 apareça.
"""
for numero_par in range(0, 21, 2):
    print(numero_par)
