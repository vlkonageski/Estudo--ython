"""
Faça um programa que calcule e mostre a soma dos 50 primeiros numeros pares.
"""
x = 1
y = 0
lista = []

while y < 50:
    if x % 2 == 0:
        lista.append(x)
        y += 1
        x += 1
    else:
        x += 1

print(lista)
print("A soma dos 50 primeiros numeros pares é: ",sum(lista))
