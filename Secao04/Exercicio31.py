"""
Leia um numero inteiro e imprima o seu antecessor e o seu sucessor.
"""

n = int(input("Informe um numero inteiro:"))

ant = n - 1
suc = n + 1

print("O antecessor de {} é {}.".format(n, ant))
print("O sucessor de {} é {}.".format(n, suc))
