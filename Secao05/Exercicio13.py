"""
Faça um algoritimo que calcule a media ponderada das notas de 3 provas. A primeira e a segunda prova
tem peso 1 e a terceira tem peso 2. Ao final, mostrar a media do aluno e indicar se o aluno foi 
aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

p1 = float(input("Informe a nota da primeira prova:"))
p2 = float(input("Informe a nota da segunda prova:"))
p3 = float(input("Informe a nota da terceira prova:"))

media = (p1 + p2 + (p3 * 2)) / 4

if media >= 60:
    print("Aluno Aprovado! Media Final {:.2f}.".format(media))
else:
    print("Aluno Reprovado! Media Final {:.2f}.".format(media))
