"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. 
A formula de conversao e: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

k = float(input("Informe a temperatura em graus Kelvin:"))

c = k - 273.15

print("{} graus Kelvin e igual a {:.2f} graus Celsius.".format(k, c))
