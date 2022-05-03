"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos.
A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo.
LEia o custo de fábrica e escreva o custo ao consumidor.
           ________________________________________________________________
          |      CUSTO DE FÁBRICA       |% DO DISTRIBUIDOR |% DOS IMPOSTOS|
          |---------------------------------------------------------------|
          |até R$12.000,00              |       5          |     isento   |
          |entre R$12.000,00 e 25.000,00|       10         |       15     |
          |acima de R$ 25.000,00        |       15         |       20     |
          |---------------------------------------------------------------|
"""

custoFabrica = float(input("Informe o custo de fabrica do veiculo:"))

if custoFabrica <= 12000:
    valorFinal = custoFabrica + (custoFabrica * 0.05)
    print("Valor final do Veiculo é R${:.2f}".format(valorFinal))
elif custoFabrica > 12000 and custoFabrica <= 25000:
    valorFinal = custoFabrica + (custoFabrica * 0.10) + (custoFabrica * 0.15)
    print("Valor final do Veiculo é R${:.2f}".format(valorFinal))
else:
    valorFinal = custoFabrica + (custoFabrica * 0.15) + (custoFabrica * 0.20)
    print("Valor final do Veiculo é R${:.2f}".format(valorFinal))
