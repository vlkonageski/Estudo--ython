"""
Leia um valor de massa em libras e apresente-o convertido em quilograma.
A formula de conversao e: K = L * 0.45, sendo K a massa em quilogramam e L a massa em libras.
"""

l = float(input("Informe a massa em libras:"))

k = l * 0.45

print("{} libras e igual a {:.2f} quilogramas.".format(l, k))
