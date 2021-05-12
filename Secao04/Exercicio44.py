"""
Receba a altura do degrau de uma escada e a altura que o usuario deseja alcancar subindo a escada.
Calcule e mostre quantos degraus o usuario devera subir para atingir seu objetivo.
"""

degrau = float(input("Informe a altura do degrau em centimetros:"))
altura = float(input("Informe a altura que deseja subir em metros:"))

calculo = int(altura / (degrau / 100))

print("Para atingir a altura de {} metros devera subir {} degraus ".format(altura, calculo))
