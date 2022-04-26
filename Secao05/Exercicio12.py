"""
Ler um numero inteiro. Se o numero lido for negativo, escreva a mensagem " numero invalido". Se o numero
for positivo. Calcular o logaritimo desse numero.
"""

import math

n = int(input("Informe um numero inteiro:"))

if n > 0:
    logaritimo = math.log(n)
    print("O logaritimo de {:d} é {:f}.".format(n , logaritimo))
else:
    print("Numero invalido!")
