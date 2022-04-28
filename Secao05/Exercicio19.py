"""
Faça um programa para verificar se um determinado numero é inteiro e divisivel por 3 ou 5,
mas nao simultaneamente pelos dois.
"""

n = int(input("Informe um numero:"))

if n % 3 == 0:
    if n % 5 == 0:
        print("{:d} é divisivel por 3 e 5!".format(n))
    else:
        print("{:d} é divisivel somente por 3!".format(n))
else:
    if n % 5 == 0:
        print("{:d} é divisivel somente por 5!".format(n))
    else:
        print("{:d} nao é divisivel nem por 3 nem por 5!".format(n))
