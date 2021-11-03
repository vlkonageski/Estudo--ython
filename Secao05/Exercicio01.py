"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""

n1 = int(input("Informe um numero:"))
n2 = int(input("Informe um numero:"))

if n1 > n2:
    print(n1, 'e maior')
elif n2 > n1:
    print(n2, 'e maior')
else:
    print('Numeros iguais')