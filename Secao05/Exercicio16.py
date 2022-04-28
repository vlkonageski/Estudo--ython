"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mes correspondente a 
este numero. Isto é, janeiro se 1, fevereiro se 2 e assim por diante.
"""

n = int(input("Informe um numero inteiro entre 1 e 12:"))

if n == 1:
    print("Janeiro")
elif n == 2:
    print("Fevereiro")
elif n == 3:
    print("Março")
elif n == 4:
    print("Abril")
elif n == 5:
    print("Maio")
elif n == 6:
    print("Junho")
elif n == 7:
    print("Julho")
elif n == 8:
    print("Agosto")
elif n == 9:
    print("Setembro")
elif n == 10:
    print("Outubro")
elif n == 11:
    print("Novembro")
elif n == 12:
    print("Dezembro")
else:
    print("Opção Invalida")
