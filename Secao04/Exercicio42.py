"""
Receba o salario-base de um funcionario. Calcule e imprima o salario a receber, sabendo-se que esse funcionario tem
uma gratificacao de 5% sobre o salario-base. Alem disso, ele paga 7% de imposto sobre o salario-base.
"""

salario_base = float(input("Informe o salario base do funcionario:"))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07

salario_liquido = salario_base + gratificacao - imposto

print("O salario a receber do funcionario e de R${:.2f}".format(salario_liquido))
