"""
Faça um programa que leia um numero inteiro positivo par N e imprima todos os numeros pares de 0 ate N em 
ordem decrescente.
"""

n = int(input("Informe um numero inteiro par:"))
x = 0
y = 0
lista = []

if n % 2 == 0:
    while y < n:
        if x % 2 == 0:
            lista.append(x)
            y += 1
            x += 1
        else:
            x += 1

    novalista = list(reversed(lista))
    print(novalista)
else:
    print(n, "Nao é numero par")

