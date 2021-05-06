"""
Leia um valor de area em metros quadrados m² e apresente-o convertido em acres.
A fórmula de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e A a area em acres.
"""

m = float(input("Informe a area em metros quadrados:"))

a = m * 0.000247

print("{} metros quadrados e igual a {:.2f} acres.".format(m, a))
