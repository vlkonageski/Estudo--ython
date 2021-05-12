"""
Faca um programa que leia um numero inteiro positivo de tres digitos( de 100 a 999).
Gere outro numero formado pelos digitos invertidos do numero lido. Exemplo:
    NumeroLido = 123
    NumeroGerado = 321.
"""

numeroLido = int(input("Inrome um numrro entre 100 e 999:"))
centena = int(numeroLido / 100)
dezena = int((numeroLido % 100) / 10)
unidade = int(numeroLido % 10)

print("Numero gerado = {}{}{}".format(unidade, dezena, centena))
