"""
Este exercício é teórico/prático.
1 - Qual comando você digitaria no terminal/cmd para instalar a biblioteca externa requests?
2 - Escreva um código Python que importe requests, faça uma requisição para 'https://www.google.com'
usando requests.get() e imprima o status_code da resposta (espera-se 200).
"""
import requests

print('Qual comando você digitaria no terminal/cmd para instalar a biblioteca externa requests?')
print('Resposta: pip install requests')

url = 'https://www.google.com'
response = requests.get(url)
print(f'{response.status_code}')
