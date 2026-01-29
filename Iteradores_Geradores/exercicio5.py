"""
1 - Crie uma classe chamada PotenciasDeDois.
2 - Implemente o método __iter__(self) que apenas retorna self.
3 - Implemente o método __next__(self). Ele deve retornar as potências de 2 (2, 4, 8, 16...).
4 - Defina um limite no __init__ (ex: até a potência 10) para que o __next__ levante StopIteration quando chegar ao fim.
5 - Teste com um for n in PotenciasDeDois(4): print(n).
"""


class PotenciasDeDois:
    def __init__(self, maxima_potencia):
        self.maxima_potencia = maxima_potencia
        self.potencia_atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.potencia_atual >= self.maxima_potencia:
            raise StopIteration

        self.potencia_atual += 1
        resultado = 2 ** self.potencia_atual

        return resultado


for n in PotenciasDeDois(4):
    print(n)
