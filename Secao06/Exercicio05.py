"""
Faça um programa que peça ao usuario para digitar 10 valores e some-os.
"""

x = 0
soma = 0
y = []

while x < 10:
    n = int(input("Informe um numero:"))
    y.append(n)
    x += 1

for z in y:
    soma = soma + z

print(soma)