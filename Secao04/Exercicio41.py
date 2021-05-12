"""
Faca um programa que leia o valor da hora de trabalho (em reais) e numeros de horas trabalhadas no mes.
Imprima o valor a ser pago ao funcionario, adicionado 10% sobre o valor do calculo.
"""

vlr_hora = float(input("Informe o valor da hora trabalhada:"))
horas_trabalhadas = int(input("Informe o numero de horas trabalhadas:"))

vlr_bruto = vlr_hora * horas_trabalhadas
vlr_liquido = vlr_bruto + (vlr_bruto * 0.10)

print("O valor a ser recebido e de R${:.2f}".format(vlr_liquido))
