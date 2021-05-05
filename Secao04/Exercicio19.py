"""
Leia um valor de volume em litros e apresente-o convertido em metros cubicos.
A formula de conversao e: M = L / 1000, sendo L o volume em litros e M o volume em metros cubicos.
"""

l = float(input("Informe o volume em litros:"))


m = l / 1000

print("{} litros e igual a {:.2f} metros cubicos".format(l, m))
