"""
Faça um algoritimo que leia um numero positivo e imprima seus divisores.
"""

n = int(input("Informe um numero inteiro positivo:"))
x = n
lista = []

while x != 0:
    if n % x == 0:
        lista.append(x)
        x -= 1
    else:
        x -= 1

print(lista)
