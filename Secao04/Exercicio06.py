"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. 
A formula de conversao e: F = C * (9 / 5) + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

c = float(input("Informe a temperatura em graus Celsius:"))

f = c * (9 / 5) + 32

print("{} graus Celsius e igual a {:.2f} graus Fahrenheit.".format(c, f))
