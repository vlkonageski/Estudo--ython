"""
Leia um valor de area em acres e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a area em acres.
"""

a = float(input("Informe a area em Acres:"))

m = a * 4048.58

print("{} acres e igual a {:.2f} metros quadrados.".format(a, m))
