"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva 
o preço novo, e escreva uma mensagem em função do preço novo ( de acordo com a segunda tabela).
            __________________________________
          |     PREÇO ANTIGO   |% DE AUMENTO  |
          | ----------------------------------|
          |até R$ 50           |     5%       |
          |entre R$ 50 e R$ 100|    10%       |
          |acima de R$ 100     |    15%       |
          |-----------------------------------|
            __________________________________
          |     PREÇO NOVO      | MENSAGEM    |
          | ----------------------------------|
          |até R$ 80            |   Barato    |
          |entre R$ 80 e R$ 120 |   Normal    |
          |entre R$ 120 e R$ 200|   Caro      |
          |acima de R$ 200      | Muito Caro  |
          |-----------------------------------|
"""

precoAntigo = float(input("Informe o preço antigo do produto:"))

if precoAntigo <= 50:
    precoNovo = precoAntigo + (precoAntigo * 0.05)
    if precoNovo <= 80:
        print("Preço Novo R${:.2f}. Barato!".format(precoNovo))
    elif precoNovo > 80 and precoNovo <= 120:
        print("Preço Novo R${:.2f}. Normal!".format(precoNovo))
    elif precoNovo > 120 and precoNovo <= 200:
        print("Preço Novo R${:.2f}. Caro!".format(precoNovo))
    else:
        print("Preço Novo R${:.2f}. Muito Caro!".format(precoNovo))
elif precoAntigo > 50 and precoAntigo <= 100:
    precoNovo = precoAntigo + (precoAntigo * 0.10)
    if precoNovo <= 80:
        print("Preço Novo R${:.2f}. Barato!".format(precoNovo))
    elif precoNovo > 80 and precoNovo <= 120:
        print("Preço Novo R${:.2f}. Normal!".format(precoNovo))
    elif precoNovo > 120 and precoNovo <= 200:
        print("Preço Novo R${:.2f}. Caro!".format(precoNovo))
    else:
        print("Preço Novo R${:.2f}. Muito Caro!".format(precoNovo))
else:
    precoNovo = precoAntigo + (precoAntigo * 0.15)
    if precoNovo <= 80:
        print("Preço Novo R${:.2f}. Barato!".format(precoNovo))
    elif precoNovo > 80 and precoNovo <= 120:
        print("Preço Novo R${:.2f}. Normal!".format(precoNovo))
    elif precoNovo > 120 and precoNovo <= 200:
        print("Preço Novo R${:.2f}. Caro!".format(precoNovo))
    else:
        print("Preço Novo R${:.2f}. Muito Caro!".format(precoNovo))