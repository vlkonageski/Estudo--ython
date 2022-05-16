"""
Faça um programa que leia 10 inteiros e imprima sua media.
"""
x = 0
y = []

while x < 10:
    n = int(input("Informe um numero:"))
    y.append(n)
    x += 1

media = sum(y)/len(y)
print(media)
