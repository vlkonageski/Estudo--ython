"""
Faça um programa que leia um numero inteiro positivo N e calcule a soma dos N primeiros numeros naturais
"""

n = int(input("Informe um numero inteiro positivo:"))
x = 0
lista = []

while x < n:
    lista.append(x)
    x += 1

print(lista)
print("A soma dos numeros é: ",sum(lista))
