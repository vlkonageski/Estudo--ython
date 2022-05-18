"""
Ler uma sequencia de numeros inteiros e determinar se eles sao pares ou nao. Devera informar o numero
de dados lidos e numero de valores pares. O processo termina quando for digitado o numero 1000.
"""

n = 0
x = 0
par = 0

while n != 1000:
    n = int(input("Informe um numero:"))
    x += 1
    if n % 2 == 0:
        par += 1

print("Foram digitados {:d} numeros. Desse numeros {:d} são pares.".format(x, par))
