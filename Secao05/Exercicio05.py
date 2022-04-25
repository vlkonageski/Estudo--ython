"""
Faça um programa que receba um numero inteiro e verifique se este numero é par ou impar.
"""

n = int(input("Informe um numero inteiro:"))

if n % 2 == 0:
    print("{:d} é par!".format(n))
else:
    print("{:d} é impar!".format(n))
