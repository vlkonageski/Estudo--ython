"""
Faça um programa que leia um numero inteiro N e depois imprima os N primeiros numeros naturais impares.
"""

n = int(input("Informe um numero inteiro:"))
x = 1
y = 0
lista = []

while y < n:
    if x % 3 == 0:
        lista.append(x)
        y += 1
        x += 1
    else:
        x += 1

print(lista)
