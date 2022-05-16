"""
Faça um programa que leia um numero inteiro positivo N e imprima todos os numeros naturais de 0 ate N em 
ordem crescente
"""

n = int(input("Informe um numero inteiro:"))
x = 0
y = 0
lista = []

while y < n:
        lista.append(x)
        y += 1
        x += 1
    

print(lista)
