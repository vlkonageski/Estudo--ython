"""
Leia um valor de volume em metros cubicos e apresente-o convertido em litros.
A formula de conversao e: L = 1000 * M, sendo L o volume em litros e M o volume em metros cubicos.
"""

m = float(input("Informe um volume em metros cubicos:"))

l = 1000 * m

print("{} metros cubicos e igual a {:.2f} litros".format(m, l))
