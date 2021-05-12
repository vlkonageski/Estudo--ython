"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o numero de dias trabalhados pelo encanador e imprima a quantia liquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda.
"""

vlr_diaria = 30

dias_trabalhados = int(input("Informe a quantidade de dias trabalhados:"))
valor_bruto = dias_trabalhados * vlr_diaria
valor_liquido = valor_bruto - (valor_bruto * 0.08)

print("O valor liquido que o encanador deve receber e de R${:.2f}".format(valor_liquido))
