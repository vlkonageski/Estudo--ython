"""
Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""

n1 = int(input("Informe um numero inteiro:"))
n2 = int(input("Informe um numero inteiro:"))

if n1 > n2:
    diferenca = n1 - n2
    print("{:d} é maior que {:d} e a diferença entre eles é de {:d}!".format(n1, n2, diferenca))
else:
    diferenca = n2 - n1
    print("{:d} é maior que {:d} e a diferença entre eles é de {:d}!".format(n2, n1, diferenca))
