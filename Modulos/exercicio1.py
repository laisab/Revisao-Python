"""
1 - Crie uma lista com 5 nomes de filmes.
2 - Use random.choice() para escolher um filme para assistir hoje e imprima.
3 - Use random.sample() para escolher 3 filmes dessa lista (sem repetir) para uma maratona.
4 - Use random.shuffle() para embaralhar a ordem da lista original e imprima o resultado.
"""

from random import choice, sample, shuffle

filmes = ['A Viagem de Chihiro',
          'Sussurros do Coração',
          'Meu Amigo Totoro',
          'O Serviço de Entregas da Kiki',
          'O Reino dos Gatos']

print(f'Filme para assistir hoje: {choice(filmes)}')
print(f'Filmes para uma maratona: {sample(filmes, 3)}')

shuffle(filmes)
print(f'Filmes: {filmes}')
