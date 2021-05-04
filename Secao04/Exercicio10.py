"""
Leia uma velocidade em Km/h (quilometros por hora) e apresente a convertida em m/s (metros por segundo).
A formula de conversao e: M = K / 3.6, sendo K a velocidade em km/h e M em m/s.
"""

k = float(input("Informe a velocidade em Km/h"))

m = k / 3.6

print("{} km/ h e igual a {:.2f} m/s".format(k, m))
