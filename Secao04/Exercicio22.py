"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros.
A formula de conversao é: M = 0.91 * J, sendo o J o comprimento em jardas e M o comprimento em metros.
"""

j = float(input("Informe o comprimento em jardas:"))

m = 0.91 * j

print("{} jardas e igual a {:.2f} metros.".format(j, m))
