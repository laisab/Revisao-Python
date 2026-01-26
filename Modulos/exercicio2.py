"""
Dado o número num = 16.
1 - Calcule a raiz quadrada de num usando uma função do módulo.
2 - Dado o ângulo angulo = 45 (graus), converta-o para radianos usando math.radians.
3 - Imprima o valor de Pi (math.pi) arredondado para 4 casas decimais.
"""

from math import sqrt, radians, pi

num = 16
print(f'Raiz quadrade de {num} = {sqrt(num)}')

angulo = 45  # graus
print(f'Ângulo em graus: {angulo}º = Ângulo em radianos: {radians(angulo)}')

print(f'Valor de π = {round(pi, 4)}')
