"""
Leia o salario de um trabalhador e o valor da prestação de um emprestimo. Se a prestação for maior que 20% do salario imprima.
Emprestimo nao concedido, caso contratio imprima: Emprestimo concedido.
"""

salario = float(input("Informe seu salario:"))
prestacao = float(input("Informe o valor da prestação:"))

if prestacao > (salario * 20) / 100:
    print("Emprestimo nao concedido!")
else:
    print("Emprestimo concedido!")