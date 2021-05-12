"""
Leia um numero inteiro de 4 digitos(de 1000 a 9999) e imprima 1 digito por linha.
"""

numero = int(input("Informe um numero de 4 digitos ente 1000 e 9999:"))

milhar = int(numero / 1000)
centena = int((numero % 1000) / 100)
dezena = int((numero % 100) / 10)
unidade = int(numero % 10)

print("{}\n{}\n{}\n{}\n".format(milhar, centena, dezena, unidade))
