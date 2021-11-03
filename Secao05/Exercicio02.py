"""
Leia um numero fornecido pelo usuario. Se esse numero for positivo, calcule a raiz quadrada do numero.
Se o numero for negativo, mostre uma mensagem dizendo que o numero é invalido.
"""
import math

n = int(input('Informe um numero:'))

if n >= 0:
    raiz = math.sqrt(n)
    print('A raiz quadrada de {} e {:.2f}'.format(n, raiz))
else:
    print('Numero invalido!')