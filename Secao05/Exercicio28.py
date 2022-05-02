"""
Faça um programa que leia tres numeros inteiro positivos e efetuo o calculo de uma das seguintes
medias de acordo com um valor numerico digitado pelo usuario:
(A) Geometrica: ³raiz X * Y * Z
(B) Ponderada: X + 2 * Y +3 * Z
                --------------
                        6
(C) Harmonica:      1
                ----------
                1 + 1 + 1
                -   -   -
                X   Y   Z

(D) Aritmetica: X + Y + Z
                ---------
                    3
"""

x = int(input("Informe o valor de X:"))
y = int(input("Informe o valor de Y:"))
z = int(input("Informe o valor de Z:"))

print("-----MENU-----\n"
"1 - Geometrica\n"
"2 - Ponderada\n"
"3 - Harmonica\n"
"4 - Aritmetica")

opcao = int(input("Informe a opção desejada:"))

if opcao == 1:
    geometrica = (x ** (1/3)) * y * z
    print("Resultado = {:.2f}".format(geometrica))
elif opcao == 2:
    ponderada = (x + 2 * y +3 * z) / 6
    print("Resultado = {:.2f}".format(ponderada))
elif opcao == 3:
    harmonica = 1 / ((1 / x) + (1 / y) + (1 / z))
    print("Resultado = {:.2f}".format(harmonica))
elif opcao == 4:
    aritmetica = (x + y + z) / 3
    print("Resultado = {:.2f}".format(aritmetica))
else:
    print("Opção Invalida!")
