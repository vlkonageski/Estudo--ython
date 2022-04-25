"""
<<<<<<< HEAD
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
=======
Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contratio imprima o 
numero ao quadrado.
"""
import math

n = int(input('Informe um numero:'))

if n >= 0:
    raiz = math.sqrt(n)
    print('A raiz quadrada de {} e {:.2f}'.format(n, raiz))
else:
    quadrado = n * n
    print('O quadrado de {} e {}'.format(n, quadrado))
>>>>>>> 702ba18eab75b2a5192eee040b7aa7646e183283
