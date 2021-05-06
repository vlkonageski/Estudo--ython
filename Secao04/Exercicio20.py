"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A formula de conversao e: L = K / 0.45, sendo K a massa em quilogramam e L a massa em libras.
"""

k = float(input("Informe a massa em quilogramas:"))

l = k / 0.45

print("{} quilogramas e igual a {:.2f} libras.".format(k, l))
