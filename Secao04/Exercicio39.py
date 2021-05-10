"""
A importancia de R$780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
º O primeiro ganhador recebera 46%
º O segundo receberá 32%
º O terceiro receberá o restante
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

valor_premio = 780000

ganhador_A = valor_premio * 0.46
ganhador_B = valor_premio * 0.32
ganhador_C = valor_premio - ( ganhador_A + ganhador_B)

print("O primeiro ganhador receberá R${:.2f} \n"
  "O segundo ganhador receberá R${:.2f} \n"
  "O terceiro ganhador receberá R${:.2f}".format(ganhador_A, ganhador_B, ganhador_C))
