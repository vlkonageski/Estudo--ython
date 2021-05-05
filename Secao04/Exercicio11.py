"""
Leia uma velocidade em m/s (metros por segundo) e apresente a convertida em Km/h (quilometros por hora).
A formula de conversao e: K = M * 3.6, sendo K a velocidade em km/h e M em m/s.
"""

m = float(input("Informe a velocidade em m/s:"))

k = m * 3.6

print("{} m/s e igual a {:.2f} km/h.".format(m, k))
