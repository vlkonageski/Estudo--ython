"""
Leia um valor em real e a cotação do dolar. Em seguida, imprima o valor correspondente em dólares.
"""

real = float(input("Informe o valor em real:"))

cotacao = float(input("Informe o valor da cotação do dolar:"))

dolar = real * cotacao

print("{} reais e igual a {:.2f} dolares".format(real, dolar))
