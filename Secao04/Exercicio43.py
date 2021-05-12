"""
Escreva um programa de ajuda para vendedores. A partir de um valor lido, mostre:
* o total a pagar com desconto de 10%
* o valor de cada parcela, no parcelamento de 3x sem juros
* a comissao do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
* a comissao do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

valor = float(input("Informe o valor do produto:"))
a_vista = valor - (valor * 0.10)
parcela = valor / 3
comissao_a_vista = a_vista * 0.05
comissao_a_prazo = valor * 0.05

print("----------AJUDA PARA VENDEDORES---------------\n"
    "Valor do produto a vista R${:.2f}\n"
    "Produto parcelado em 3x de R${:.2f}\n"
    "Comissao do vendendo venda a vista R${:.2f}\n"
    "Comissao vendedor venda a prazo R${:.2f}\n"
    "------------------------------------------------"
    .format(a_vista, parcela, comissao_a_vista, comissao_a_prazo))
