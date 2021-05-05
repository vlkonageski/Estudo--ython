"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A formula de conversao e: C = P * 2.54, sendo C o comprimento em centimetros e P em polegadas.
"""

p = float(input("Informe o comprimento em polegadas:"))

c = p * 2.54

print("{} polegadas e igual a {:.2f} centimetros".format(p, c))
