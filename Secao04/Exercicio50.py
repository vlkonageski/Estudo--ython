"""
Faca um programa para ler as dimensoes de um terreno (comprimento C e largura L),
bem como o preco do metro de tela P. Imprima o custo para cercar este mesmo terreno com tela.
"""

c = float(input("Informe o comprimento do terreno:"))
l = float(input("Informe a largura do terreno:"))
p = float(input("Informe o preço do metro da tela:"))

tamanho = c * l
valor = tamanho * p

print("O valor para cercar o lote de {} m² e de R${:.2f}".format(tamanho, valor))
