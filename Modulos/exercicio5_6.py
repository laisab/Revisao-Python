"""
Parte 2: Módulos Customizados (Seus Arquivos)
   Para os exercícios 5 e 6, imagine que você está criando dois arquivos na mesma pasta.
-> Exercício 5: Criando a Biblioteca (moeda.py)
1 - Crie um código que represente o conteúdo de um arquivo chamado moeda.py.
2 - Neste arquivo, defina duas funções:
*   aumentar(valor, porcentagem): Retorna o valor acrescido da porcentagem.
*   diminuir(valor, porcentagem): Retorna o valor subtraído da porcentagem.

-> Exercício 6: Importando a Biblioteca (main.py)
1 - Agora crie o código do arquivo principal main.py.
2 - Importe o módulo moeda (criado no exercício anterior).
3 - Crie uma variável preco = 100.
4 - Use a função moeda.aumentar para subir o preço em 10% e imprima o resultado.
* Desafio: Tente importar apenas a função diminuir usando from ... import ...
  e use-a para baixar o preço original em 5%.
"""
import moeda
from moeda import diminuir

preco = 100

preco_aumentado = moeda.aumentar(preco, 10)
print(f'Preço original = R${preco}\nPreço com aumento de 10% = R${preco_aumentado}')

preco_diminuido = diminuir(100, 5)
print(f'\nPreço original = R${preco}\nPreço com diminuição de 5% = R${preco_diminuido}')
