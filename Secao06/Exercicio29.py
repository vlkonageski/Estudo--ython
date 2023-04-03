"""
Escreva um programa para calcular o valor da serie, para 5 termos.
        S=0 + 1/2 + 2/4 + 3/6 + ...
"""

x = 1
y = 2
lista = []
while x != 6:
    z = x/y
    lista.append(z)
    x += 1
    y += 2

print(lista)
print(sum(lista))
