"""
Leia um angulo em graus e apresente-o convertido em radianos.
A formula de conversao e: R = G * π / 180, sendo G o angulo em graus e R em radianos e π = 3.14
"""

g = float(input("Informe o angulo em graus:"))

r = g * 3.14 / 180

print("{} graus e igual a {:.2f} radianos.".format(g, r))
