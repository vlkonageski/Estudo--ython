"""
Leia um numero inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""

n = int(input("Informe um numero inteiro:"))

suc = (n * 3) + 1
ant = (n * 2) - 1

soma = suc + ant

print("A soma do sucessor do triplo com o antecessor do dobro do numero {} é igual a: {}".format(n, soma))
