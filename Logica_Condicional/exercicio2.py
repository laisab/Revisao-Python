"""
Agora precisamos tomar decisões com mais de duas opções.

1 - Crie uma variável para temperatura com algum valor.
2 - Classifique o clima:
*   Menor que 15: Imprima "Está frio!"
*   Entre 15 e 29 (inclusive): Imprima "Está agradável!"
*   30 ou mais: Imprima "Está muito quente!"
"""
temperatura = 22

if temperatura < 15:
    print(f'Está frio!')
elif 15 <= temperatura <= 29:
    print(f'Está agradável!')
else:
    print(f'Está muito quente!')
