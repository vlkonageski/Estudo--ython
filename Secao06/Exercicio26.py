"""
Faça um algoritimo que encontre o primeiro multiplo de 11, 13 ou 17 apos o numero dado.
"""

n = int(input("Informe um numero:"))

while n != 0:
    if n % 17 == 0 or n % 13 == 0 or n % 11 == 0:
        if n % 17 == 0:
            print(f"O numero é {n} e é multiplo de 17!")
            break
        elif n % 13 == 0:
            print(f"O numero é {n} e é multiplo de 13!")
            break
        else:
            print(f"O numero é {n} e é multiplo de 11!")
            break
    else:
        n -= 1
