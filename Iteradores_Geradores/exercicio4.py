"""
1 - Crie uma Lista com os números de 0 a 10.000.
2 - Crie uma Expressão Geradora (Generator Expression) com os mesmos números.
3 - Use sys.getsizeof() para imprimir o tamanho em bytes de cada variável.
* Objetivo: Ver a diferença brutal de tamanho entre carregar tudo na memória (lista) vs carregar sob demanda (gerador).
"""
import sys

lista_numeros = [x for x in range(10001)]
expressao_geradora = (x for x in range(10000))

print(f"Tamanho - lista (memória): {sys.getsizeof(lista_numeros)}")
print(f"Tamanho - generator (sob demanda): {sys.getsizeof(expressao_geradora)}")
