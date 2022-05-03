"""
Escrever um programa que leia o codigo do produto escolhido do cardapio de uma lanchonete e a 
quantidade.O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada 
execução somente será calculado um pedido. O cardapio da lanchonete segue o padrao abaixo:
           _____________________________________
          |ESPECIFICAÇÃO  | CODIGO |   PREÇO    |
          |-------------------------------------|
          |Cachorro quente|  100   |    1,20    |
          |Bauru simples  |  101   |    1,30    |
          |Bauru com ovo  |  102   |    1,50    |
          |Hamburguer     |  103   |    1,20    |
          |Cheeseburguer  |  104   |    1,70    |
          |Suco           |  105   |    2,20    |
          |Refrigerante   |  106   |    1,00    |
          |-------------------------------------|
"""

codigo = int(input("Informe o codigo do produto:"))
quantidade = int(input("Informe a quantidade:"))

if codigo == 100:
    valor = quantidade * 1.20
    print("O pedido foi de {:d} Cachorro quente. Valor R${:.2f}".format(quantidade, valor))
elif codigo == 101:
    valor = quantidade * 1.30
    print("O pedido foi de {:d} Bauru Simples. Valor R${:.2f}".format(quantidade, valor))
elif codigo == 102:
    valor = quantidade * 1.50
    print("O pedido foi de {:d} Bauru com ovo. Valor R${:.2f}".format(quantidade, valor))
elif codigo == 103:
    valor = quantidade * 1.20
    print("O pedido foi de {:d} Hamburguer. Valor R${:.2f}".format(quantidade, valor))
elif codigo == 104:
    valor = quantidade * 1.70
    print("O pedido foi de {:d} Cheeseburguer. Valor R${:.2f}".format(quantidade, valor))
elif codigo == 105:
    valor = quantidade * 2.20
    print("O pedido foi de {:d} Suco. Valor R${:.2f}".format(quantidade, valor))
elif codigo == 106:
    valor = quantidade * 1.00
    print("O pedido foi de {:d} Refrigerante. Valor R${:.2f}".format(quantidade, valor))
else:
    print("Codigo Invalido!")
