"""
Leia um angulo em radianos e apresente-o convertido em graus.
A formula de conversao e: G = R * 180 / π, sendo G o angulo em graus e R em radianos e π = 3.14
"""

r = float(input("Informe o angulo em radianos:"))

g = r * 180 / 3.14

print("{} radianos e igual a {:.2f} graus".format(r, g))
