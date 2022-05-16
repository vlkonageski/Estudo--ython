"""
Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor lido.
"""

n = 0
lista = []

while n < 10:
    x = int(input("Informe um numero:"))
    n += 1
    lista.append(x)


print("O maior numero é {:d} e o menor numero é {:d}".format(max(lista), min(lista)))
