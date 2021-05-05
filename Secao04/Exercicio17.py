"""
Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas.
A formula de conversao e: P = C / 2.54, sendo C o comprimento em centimetros e P em polegadas.
"""

c = float(input("Informe o comprimento em centimetros:"))

p = c / 2.54

print("{} centimetros e igual a {:.2f} polegadas".format(c, p))
