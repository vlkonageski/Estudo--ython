"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequencia arbitraria de notas
(validas no intervalo de 10 a 20) e que mostre na tela como resultado, a correspondente media aritimetica. O numero
de notas com que o aluno prentende efetuar o calculo nao sera fornecido ao programa, o qual terminara quando for
introduzido um valor que nao seja valido como nota de aprovação.
"""

nome = input("Informe o nome do Aluno:")
notas = float(input("Informe a nota:"))
qtd_notas = 0
lista = []

while notas >= 10 and notas <= 20:
    qtd_notas += 1
    lista.append(notas)
    notas = int(input("Informe a nota:"))

media = sum(notas) / qtd_notas

print("A media do Aluno {} foi {}!".format(nome, media))
