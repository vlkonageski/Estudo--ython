"""
Faça um programa que calcule e mostre a area de um trapezio. Sabe-se que:
            A = (basemaior + basemenor) * altura
            ------------------------------------
                            2
Lembre-se a base maior e a base menor devem ser numeros maiores que zero.
"""

basemaior = float(input("Informe o tamanho da base maior:"))

if basemaior > 0:
    basemenor = float(input("Informe o tamanho da base menor:"))
    if basemenor > 0:
        altura = float(input("Informe a altura:"))
        a = ((basemaior + basemenor) * altura) / 2
        print("A area do trapezio é {:.2f}.".format(a))
    else:
        print("A base menor deve ser maior que zero!")
else:
    print("A base maior deve ser maior que zero!")
