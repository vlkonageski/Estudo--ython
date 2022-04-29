"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente
de imposto sobre o produto( MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuario entre com o
valor e o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do
estado em que ele será vendido. Se o estado nao for valido, mostrar uma mensagem de erro.
"""

valor = float(input("Informe o valor da venda R$:"))
estado = input("Informe o estado da venda:")

if estado == 'MG' or estado == 'mg':
    imposto = (valor * 7) / 100
    vlr_final = valor + imposto 
    print("Valor venda R${:.2f} + R${:.2f} de imposto, valor final R${:.2f}.".format(valor, imposto, vlr_final))
elif estado == 'SP' or estado == 'sp':
    imposto = (valor * 12) / 100
    vlr_final = valor + imposto
    print("Valor venda R${:.2f} + R${:.2f} de imposto, valor final R${:.2f}.".format(valor, imposto, vlr_final))
elif estado == 'RJ' or estado == 'rj':
    imposto = (valor * 15) / 100
    vlr_final = valor + imposto
    print("Valor venda R${:.2f} + R${:.2f} de imposto, valor final R${:.2f}.".format(valor, imposto, vlr_final))
elif estado == 'MS' or estado == 'ms':
    imposto = (valor * 8) / 100
    vlr_final = valor + imposto
    print("Valor venda R${:.2f} + R${:.2f} de imposto, valor final R${:.2f}.".format(valor, imposto, vlr_final))
else:
    print("Não vendemos para este estado!")
