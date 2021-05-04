"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. 
A formula de conversao e: K = C + 273.15, sendo K a temperatura em Kelvin e C a temperatura em Celsius.
"""

c = float(input("Informe a temperatura em graus Celsius:"))

k = c + 273.15

print("{} graus Celsius e igual a {:.2f} graus Kelvin".format(c, k))
