"""
Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação esolhida.
Escreva uma mensagem de erro se a opção for invalida.
 1- Soma de dois numeros
 2- Diferença entre 2 numeros (maior pelo menor)
 3- Produto entre 2 numeros
 4- Divisao entre dois numeros (o denominador nao pode ser zero.)
 Opção
"""

print("----MENU----\n"
 "1- Soma de dois numeros\n"
 "2- Diferença entre 2 numeros (maior pelo menor)\n"
 "3- Produto entre 2 numeros\n"
 "4- Divisao entre dois numeros (o denominador nao pode ser zero.)")

opcao = int(input("Informe a opção desejada:"))

if opcao == 1:
    n1 = int(input("Informe o primeiro numero:"))
    n2 = int(input("Informe o segundo numero:"))
    soma = n1 + n2
    print("A soma de {:d} + {:d} = {:d}".format(n1, n2, soma))
elif opcao == 2:
    n1 = int(input("Informe o primeiro numero:"))
    n2 = int(input("Informe o segundo numero:"))
    if n1 > n2:
        diferenca = n1 - n2
        print("A diferença de {:d} - {:d} = {:d}".format(n1, n2, diferenca))
    else:
        diferenca = n2 - n1
        print("A diferença de {:d} - {:d} = {:d}".format(n2, n1, diferenca))
elif opcao == 3:
    n1 = int(input("Informe o primeiro numero:"))
    n2 = int(input("Informe o segundo numero:"))
    produto = n1 * n2
    print("O produto de {:d} * {:d} = {:d}".format(n1, n2, produto))
elif opcao == 4:
    n1 = int(input("Informe o primeiro numero:"))
    n2 = int(input("Informe o segundo numero:"))
    if n2 == 0:
        print("O denominador nao pode ser zero!")
    else:
        divisao = n1 / n2
        print("A divisao de {:d} / {:d} = {:.2f}".format(n1, n2, divisao))
else:
    print("Opção Invalida!")
