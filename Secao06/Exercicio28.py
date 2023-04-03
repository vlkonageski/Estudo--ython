"""
Faça um programa q leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a formula a seguir.

    E = 1 + 1/1 + 1/2 + 1/3 ... + 1/N
"""

n = int(input("Informe um numero inteiro positivo:"))
x = 1
y = 1
lista = []
while x != n:
    z = y/x
    lista.append(z)
    x += 1

print(lista)
print(sum(lista))
