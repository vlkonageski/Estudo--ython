"""
Faça um programa que mostre ao usuario um menu com 4 opções de operações matematicas
(as básicas, por exemplo).O usuário escolhe uma das opções e o seu programa entao pede dois valores
numéricos e realiza a operação, mostrando o resultado e saindo.
"""

print("-----MENU-----\n"
    "1 - Adição\n"
    "2 - Subtração\n"
    "3 - Multiplicação\n"
    "4 - Divisão")

opcao = int(input("Informe a opção desejada:"))

if opcao == 1:
    n1 = int(input("Informe o primeiro numero:"))
    n2 = int(input("Informe o segundo numero:"))
    soma = n1 + n2
    print("A soma de {:d} + {:d} = {:d}".format(n1, n2, soma))
elif opcao == 2:
    n1 = int(input("Informe o primeiro numero:"))
    n2 = int(input("Informe o segundo numero:"))
    subtracao = n1 - n2
    print("A subtração de {:d} - {:d} = {:d}".format(n1, n2, subtracao))
elif opcao == 3:
    n1 = int(input("Informe o primeiro numero:"))
    n2 = int(input("Informe o segundo numero:"))
    multiplicacao = n1 * n2
    print("A multiplicação de {:d} * {:d} = {:d}".format(n1, n2, multiplicacao))
elif opcao == 4:
    n1 = int(input("Informe o primeiro numero:"))
    n2 = int(input("Informe o segundo numero:"))
    divisao = n1 / n2
    print("A divisao de {:d} / {:d} = {:.2f}".format(n1, n2, divisao))
else:
    print("Opção Invalida!")
