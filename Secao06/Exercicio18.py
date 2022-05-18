"""
Escreva um algoritimo que leia certa quantidade de numeros e imprima o maior deles e quantas vezes o 
maior numero foi lido. A quantidade de numeros a serem lidos deve ser fornecida pelo usuario.
"""

n = int(input("Informe quantos numeros deseja informar:"))
x = 0
lista = []
qtd = 0

while x < n:
    y = int(input("Informe um numero:"))
    lista.append(y)
    x += 1

maior = max(lista)

for z in lista:
    if z == maior:
        qtd += 1

print("O maior numero na lista é {:d} ele repete {:d} vezes.".format(maior, qtd))
