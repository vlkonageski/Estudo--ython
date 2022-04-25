"""
Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
º O numero digitado ao quadrado
º A raiz quadrada do numero digitado.
"""
<<<<<<< HEAD

import math

n = float(input("Informe um numero:"))

if n > 0:
    quadrado = n * n
    raiz = math.sqrt(n)
    print("O quadrado de {} é {:.2f}!".format(n, quadrado))
    print("A raiz quadrada de {} é {:.2f}!".format(n, raiz))
else:
    print("Numero Invalido!")
=======
import math

n = int(input('Informe um numero:'))

if n >= 0:
    quadrado = n * n
    print('O quadrado de {} e {}'.format(n, quadrado))
else:
    raiz = math.sqrt(n)
    print('A raiz quadrada de {} e {:.2f}'.format(n, raiz))
>>>>>>> 702ba18eab75b2a5192eee040b7aa7646e183283
