"""
Em matematica, o numero harmonico designado por H(n) define-se como sendo a soma da serie harmonica:
                H(n) = 1 + 1/2 + 1/3 + 1/4 + ... 1/n
Faça um programa que leia um valor (n) inteiro e positivo e apresente o valor de H(n).
"""

n = int(input("Informe um numero inteiro positivo:"))
x = 1
y = 1
lista = []
while x != n:
    z = y/x
    lista.append(z)
    x += 1

print(lista)
print(sum(lista))
