"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi 
de 12%.
"""

valor_produto = float(input("Informe o valor do produto:"))
desconto = 0.12

valor_final = valor_produto - (valor_produto * desconto)

print("O valor do produto com desconto e de R${:.2f}".format(valor_final))
