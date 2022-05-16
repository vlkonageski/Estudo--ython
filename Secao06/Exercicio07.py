"""
Faça um programa que leia 10 inteiros positivos, ignorando nao positivos, e imprima sua media.
"""

x = 0
lista = []

while x < 10:
    n = int(input("Informe um numero inteiro:"))
    if n > 0:
        lista.append(n)
        x += 1

media = sum(lista)/len(lista)
print(media)
