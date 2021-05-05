"""
Leia uma distancia em milhas e apresente-a convertida em quilometros.
A formula de conversao e: K = 1.6 * M, sendo K a distancia em quilometros e M em milhas..
"""

m = float(input("Informe a distancia em milhas:"))

k = 1.6 * m

print("{} milhas e igual a {:.2f} quilometros.".format(m, k))
