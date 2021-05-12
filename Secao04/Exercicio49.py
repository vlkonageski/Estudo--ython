"""
Tres amigos jogaram na loteria. Caso eles ganhem o premio deve ser repartido proporcionalmente ao valor que cada
deu para a realizacao da aposta. Faca um programa que leia quanto cada apostador investiu, o valor do premio, e 
imprima quanto cada um ganharia do premio com base no valor investido.
"""

ap1 = float(input("Informe o valor investido pelo primeiro apostador:"))
ap2 = float(input("Informe o valor investido pelo segundo apostador:"))
ap3 = float(input("Informe o valor investido pelo terceiro apostador:"))
vlr_aposta = ap1 + ap2 + ap3

vlr_premio = float(input("Informe o valor do prêmio:"))

premio_ap1 = (vlr_premio * ap1) / vlr_aposta
premio_ap2 = (vlr_premio * ap2) / vlr_aposta
premio_ap3 = (vlr_premio * ap3) / vlr_aposta

print("-----PREMIO TOTAL R${:.2f}-------\n"
    "Apostador 1 receberá R${:.2f}\n"
    "Apostador 2 receberá R${:.2f}\n"
    "Apostador 3 receberá R${:.2f}"
    .format(vlr_premio, premio_ap1, premio_ap2, premio_ap3))
