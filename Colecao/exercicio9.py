"""
Exercício 9: Ficha de Carro (NamedTuple)
NamedTuple cria objetos simples que parecem classes, mas consomem pouca memória.

1 - Defina uma estrutura chamada Carro com os campos ['marca', 'modelo', 'ano'].
2 - Crie uma instância: meu_carro = Carro(marca="Toyota", modelo="Corolla", ano=2020).
3 - Imprima apenas a marca do carro acessando pelo nome do atributo.
"""

from collections import namedtuple

carro = namedtuple('carro', 'marca modelo ano')
meu_carro = carro(marca='Toyota', modelo='Corolla', ano=2020)

print(f'Marca do carro: {meu_carro.marca}')
