"""
Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
"""

idade = int(input("Informe a sua idade:"))
ano_atual = int(input("Informe o ano atual:"))

ano_nascimento = ano_atual - idade

print("O seu ano de nascimento e:", ano_nascimento)
