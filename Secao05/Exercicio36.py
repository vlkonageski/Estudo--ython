"""
Escreva um programa que, dado o valor da venda, imprima a comissao que deverá ser paga ao vendedor.
Para calcular a comissao, considere a tabela abaixo:
           _______________________________________________________________________________
          |                    VENDA MENSAL                     |      COMISSAO           |
          |-------------------------------------------------------------------------------|
          |Maior ou igual a R$100.000,00                        |R$700,00 + 16% das vendas|
          |Menor que R$100.000,00 e maior ou igual a R$80.000,00|R$650,00 + 14% das vendas|
          |Menor que R$80.000,00 e maior ou igual a R$60.000,00 |R$600,00 + 14% das vendas|
          |Menor que R$60.000,00 e maior ou igual a R$40.000,00 |R$550,00 + 14% das vendas|
          |Menor que R$40.000,00 e maior ou igual a R$20.000,00 |R$500,00 + 14% das vendas|
          |Menor que R$20.000,00                                |R$400,00 + 14% das vendas|
          |-------------------------------------------------------------------------------|
"""

vlrVenda = float(input("Informe o valor das vendas:"))

if vlrVenda >= 100000:
    comissao = 700 + (vlrVenda * 0.16)
    print("A comissao a ser paga e de R${:.2f}".format(comissao))
elif vlrVenda > 100000 and vlrVenda >= 80000:
    comissao = 650 + (vlrVenda * 0.14)
    print("A comissao a ser paga e de R${:.2f}".format(comissao))
elif vlrVenda > 80000 and vlrVenda >= 60000:
    comissao = 600 + (vlrVenda * 0.14)
    print("A comissao a ser paga e de R${:.2f}".format(comissao))
elif vlrVenda > 60000 and vlrVenda >= 40000:
    comissao = 550 + (vlrVenda * 0.14)
    print("A comissao a ser paga e de R${:.2f}".format(comissao))
elif vlrVenda > 40000 and vlrVenda >= 20000:
    comissao = 500 + (vlrVenda * 0.14)
    print("A comissao a ser paga e de R${:.2f}".format(comissao))
else:
    comissao = 400 + (vlrVenda * 0.14)
    print("A comissao a ser paga e de R${:.2f}".format(comissao))
