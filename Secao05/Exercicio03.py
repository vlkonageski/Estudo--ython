"""
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
