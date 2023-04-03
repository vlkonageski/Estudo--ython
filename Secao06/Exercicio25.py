"""
Faça um programa que some todos os numeros naturais abaixo de 1000 que sao multiplos de 3 ou 5.
"""
n = 1000
lista = []

while n != 0:
    if n % 5 == 0 or n % 3 == 0:
        lista.append(n)
        n -= 1
    else:
        n -= 1

print(lista)
print(sum(lista))
