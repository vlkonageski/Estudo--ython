"""
Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
º O numero digitado ao quadrado
º A raiz quadrada do numero digitado.
"""
import math

n = int(input('Informe um numero:'))

if n >= 0:
    quadrado = n * n
    print('O quadrado de {} e {}'.format(n, quadrado))
else:
    raiz = math.sqrt(n)
    print('A raiz quadrada de {} e {:.2f}'.format(n, raiz))
