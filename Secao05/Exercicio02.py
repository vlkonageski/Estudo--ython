"""
Leia um numero fornecido pelo usuario. Se esse numero for positivo, calcule a raiz quadrada do numero.
Se o numero for negativo, mostre uma mensagem dizendo que o numero é invalido.
"""
<<<<<<< HEAD

import math

n = int(input("Informe um numero:"))

if n > 0:
    raiz = math.sqrt(n)
    print("A raiz quadrada de {:d} é {:.2f}!".format(n, raiz))
else:
    print("Número invalido!")
=======
import math

n = int(input('Informe um numero:'))

if n >= 0:
    raiz = math.sqrt(n)
    print('A raiz quadrada de {} e {:.2f}'.format(n, raiz))
else:
    print('Numero invalido!')
>>>>>>> 702ba18eab75b2a5192eee040b7aa7646e183283
