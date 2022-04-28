"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana
correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""

opcao = int(input("Informe um numero de 1 a 7:"))

if opcao == 1:
    print("Domingo")
elif opcao == 2:
    print("Segunda-Feira")
elif opcao == 3:
    print("Terça-Feira")
elif opcao == 4:
    print("Quarta-Feira")
elif opcao == 5:
    print("Quinta-Feira")
elif opcao == 6:
    print("Sexta-Feira")
elif opcao == 7:
    print("Sabado")
else:
    print("Opção Invalida!")
