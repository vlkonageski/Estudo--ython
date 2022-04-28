"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo e, se forem,
se é um triangulo escaleno, equilatero ou isoscele, considerando os seguintes conceitos.
 º O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
 º Chama-se equilatero o triangulo que tem tres lados iguais
 º Denomina-se isosceles o triangulo que tem o comprimento de dois lados iguais.
 º Recebe o nome de escaleno o triangulo que tem os tres lados diferentes.
"""

a = float(input("Informe o tamanho do lado A:"))
b = float(input("Informe o tamanho do lado B:"))
c = float(input("Informe o tamanho do lado C:"))

if a < b + c and b < c + a and c < a + b:
    if a == b == c:
        print("Triangulo Equilatero")
    elif a == b or b == c or a == c:
        print("Triangulo Isosceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Não é um triangulo!")
