"""
Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contratio imprima o numero
ao quadrado.
"""

import math


n = float(input("Informe um numero real:"))

if n > 0:
    raiz = math.sqrt(n)
    print("A raiz quadrada de {:.2f} é {:.2f}!".format(n, raiz))
else:
    quadrado = n * n
    print("O quadrado de {:.2f} é {:.2f}!".format(n, quadrado))
