"""
Dado o código abaixo com um breakpoint():

x = 10
y = 5
breakpoint()
z = x * y
y = 0
w = x / y
print("Fim")

Imagine que você está no terminal rodando o PDB.
1 - Ao parar no breakpoint, qual o valor de z se você digitar o comando p z?
(Dica: a linha do z já foi executada ou ainda vai ser?)
2 - Se você der o comando n (next) uma vez, em qual linha o depurador vai parar?
3 - Se você continuar executando (c ou n até o fim), qual erro vai acontecer na linha w = x / y?
"""

x = 10
y = 5
breakpoint()
z = x * y
y = 0
w = x / y
print("Fim")

print('1 - NameError')
print('2 - Depurador vai para y = 0')
print('3 - ZeroDivisionError')
