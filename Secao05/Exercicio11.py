"""
Escreva um programa que leia um numero inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarismos. Por exemplo, ao numero 251 corresponderá o valor 8 (2 + 5 + 1).
Se o numero lido nao for maior do que zero, o programa terminará com a mensagem "Numero inválido"
"""

n = int(input("Informe um numero inteiro:"))

if n > 0:
    centena = int(n / 100)
    dez = int((n % 100) / 10)
    uni = int(n % 10)
    soma = centena + dez + uni
    print("{:d} + {:d} + {:d} = {:d}".format(centena, dez, uni, soma))
else:
    print("Numero Invalido!")