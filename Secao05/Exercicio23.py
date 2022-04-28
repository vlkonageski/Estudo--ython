"""
Determine se um determinado ano lido é bisexto. Sendo que um ano é bisexto se for divisivel por 400
ou se for divisivel por 4 e nao for divisiel por 100. por exemplo 1988, 1992, 1996.
"""

ano = int(input("Informe o ano que deseja saber se é bissexto:"))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print("{:d} é ano bissexto!".format(ano))
else:
    print("{:d} não é ano bissexto!".format(ano))
