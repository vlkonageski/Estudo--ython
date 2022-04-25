"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde H corresponde a altura):
º Homens: (72.7 * H) - 58
º Mulheres: (62.1 * H) - 44.7
"""

h = float(input("Informe a sua altura:"))
s = input("Informe M para Homem e F para Mulher:")

if s == 'M' or s == 'm':
    pesoIdeal = (72.7 * h) - 58
    print("O seu peso ideal é {:.2f}!".format(pesoIdeal))
elif s == 'F' or s == 'f':
    pesoIdeal = (62.1 * h) - 44.7
    print("O seu peso ideal é {:.2f}!".format(pesoIdeal))
