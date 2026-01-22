"""
Crie um programa que tenta converter um input do usuário em número.
1 - Peça ao usuário: "Digite um número".
2 - Use um bloco try para converter a entrada para float e realizar a conta 100 / numero.
3 - Use except ValueError: Imprima "Erro: Você precisa digitar um número numérico".
4 - Use except ZeroDivisionError: Imprima "Erro: Não é possível dividir por zero".
5 - Use else: Imprima "Cálculo realizado com sucesso: [resultado]".
6 - Use finally: Imprima "Operação finalizada" (aparece sempre).
"""
numero = input('Digite um número: ')

try:
    numero = float(numero)
    resultado = 100 / numero
except ValueError:
    print("Erro: Você precisa digitar um número numérico")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero")
else:
    print(f"Cálculo realizado com sucesso: {resultado}")
finally:
    print("\nOperação finalizada")
