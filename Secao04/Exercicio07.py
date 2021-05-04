"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 
A formula de conversao e: C = 5 * (F - 32) / 9, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""

f = float(input("Informe a temperatura em graus Fahrenheit:"))

c = 5 * (f - 32) / 9

print("{} graus Fahrenheit e igual a {:.2f} graus Celsius.".format(f, c))
