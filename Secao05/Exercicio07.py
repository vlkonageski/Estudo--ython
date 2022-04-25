"""
Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois numeros forem iguais,
imprima a mensagem numeros iguais.
"""

n1 = int(input("Informe um numero:"))
n2 = int(input("Informe um numero:"))

if n1 > n2:
    print("{:d} é o numero maior!".format(n1))
elif n2 > n1:
    print("{:d} é o numero maior!".format(n2))
else:
    print("Os numeros são iguais!")
