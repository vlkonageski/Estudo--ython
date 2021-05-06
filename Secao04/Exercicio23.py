"""
Leia um valor de comprimento em metros e apresente-o convertido em jardas.
A formula de conversao é: J = M / 0.91, sendo o J o comprimento em jardas e M o comprimento em metros.
"""

m = float(input("Informe o comprimento em metros:"))

j = m / 0.91

print("{} metros e igual a {:.2f} jardas.".format(m, j))
