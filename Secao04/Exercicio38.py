"""
Leia o salario de um funcionario. Calcule e imprima o valor do novo salario, sabendo que ele recebeu um aumento
de 25%.
"""

salario = float(input("Informe o salario do funcionario:"))
aumento = 0.25

novo_salario = salario + (salario * aumento)

print("O novo salario do funcionario será de R${:.2f}".format(novo_salario))
