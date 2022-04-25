"""
Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
º O numero digitado ao quadrado
º A raiz quadrada do numero digitado.
"""

import math

n = float(input("Informe um numero:"))

if n > 0:
    quadrado = n * n
    raiz = math.sqrt(n)
    print("O quadrado de {} é {:.2f}!".format(n, quadrado))
    print("A raiz quadrada de {} é {:.2f}!".format(n, raiz))
else:
    print("Numero Invalido!")
