"""
Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:
          _________________________________
          |   IMC      |   CLASSIFICAÇÃO  |
          |-------------------------------|
          |< 18,5      |Abaixo do Peso    |
          |18,6 - 24,9 |Saudavel          |
          |25,0 - 29,9 |Peso em excesso   |
          |30,0 - 34,9 |Obesidade Grau I  |
          |35,0 - 39,9 |Obesidade Grau II |
          |>= 40,0     |Obesidade Grau III|
          |-------------------------------|
"""

peso = float(input("Informe seu peso:"))
altura = float(input("Informe sua altura:"))
imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do peso!")
elif imc > 18.5 and imc < 25:
    print("Saudavel!")
elif imc >= 25 and imc < 30:
    print("Peso em excesso!")
elif imc >= 30 and imc < 35:
    print("Obesidade Grau I!")
elif imc >= 35 and imc < 40:
    print("Obesidade Grau II!")
else:
    print("Obesidade Grau III!")
