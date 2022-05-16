"""
Faça um programa que determine e mostre os 5 primeiros multiplos de 3, considerando numeros maiores que 0.
"""

x = 0
n = 1
y = []

while x < 5:
    if n % 3 == 0:
        y.append(n)
        n += 1
        x += 1
    else:
        n += 1

print(y)
