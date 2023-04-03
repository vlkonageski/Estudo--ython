"""
Escreva um programa que leia um numero inteiro e calcule a soma de todos os divisores desse numero, com exceção
dele proprio. Ex:  a soma dos divisores do numero 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""

n =  int(input("Informe um numero inteiro:"))
x = n
lista = []

while x != 0:
    if n % x == 0 and n != x:
        lista.append(x)
        x -= 1
    else:
        x -= 1

print(lista)
print(sum(lista))
