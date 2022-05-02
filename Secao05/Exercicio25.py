"""
Calcule as raizes da equação de 2º grau.
            Lembrando que:
            x = -b+- raiz delta
                ---------------
                    2a
                    Onde
                delta = B² - 4ac

E ax² + bx + c = ) representa uma equação de 2º grau.
A variavel A tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não é equação de segundo grau".
 ºSe delta < 0, nao existe real. Imprima a mensagem "Nao existe raiz"
 ºSe delta = 0, existe uma raiz real. Imprima a raiz e a mensagem "Raiz unica".
 ºSe delta >= 0, imprima as duas raizes reais.
"""

a = int(input("Informe o valor de A:"))
b = int(input("Informe o valor de B:"))
c = int(input("Informe o valor de C:"))
delta = (b * b) - (4 * a * c)

if delta < 0:
    print("Não existe raiz!")
elif delta == 0:
    print("Raiz unica!")
else:
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print(" x¹= {:.2f} e x² = {:.2f}".format(x1, x2))
