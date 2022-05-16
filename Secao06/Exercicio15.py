"""
Faça um programa que leia um numero inteiro positivo impar N e imprima todos os numeros impares de 1 ate N em 
ordem crescente.
"""


n = int(input("Informe um numero inteiro impar:"))
x = 0
y = 0
lista = []

if n % 3 == 0:
    while y < n:
        if x % 3 == 0:
            lista.append(x)
            y += 1
            x += 1
        else:
            x += 1

    print(lista)
else:
    print(n, "Nao é numero impar")

