"""
Faça um programa que receba dois numeros. Calcule e mostre:
    ° a soma dos numeros pares desse intervalo de numeros, incluindo os numeros digitados.
    ° a multiplicação dos numeros impares desse intervalo, incluindo os digitados.
"""

n1 = int(input("Informe o primeiro numero:"))
n2 = int(input("Informe o segundo numero:"))
soma = 0
multiplicacao = 0


while n1 <= n2:
    if n1 % 2 == 0:
        soma += n1
        n1 += 1
    else:
        multiplicacao = n1 * n1
        n1 += 1

print("A soma dos numeros pares e {} e a multiplicacao dos numeros impares e {}!" .format(soma, multiplicacao))
