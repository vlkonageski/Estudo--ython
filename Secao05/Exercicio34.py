"""
Leia a nota e o numero de faltas de um aluno, e escreva seu conceito.
De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.
           ________________________________________________
          |    NOTA     | Até 20 faltas | Mais de 20 faltas|
          |------------------------------------------------|
          |9.0 ate 10.0 |       A       |       B          |
          |7.5 ate 8.9  |       B       |       C          |
          |5.0 ate 7.4  |       C       |       D          |
          |4.0 ate 4.9  |       D       |       E          |
          |0.0 ate 3.9  |       E       |       E          |
          |------------------------------------------------|
"""

nota = float(input("Informe a nota do aluno:"))
faltas = int(input("Informe o numero de faltas do aluno:"))

if nota >= 9 and nota <= 10:
    if faltas <= 20:
        print("Conceito A")
    else:
        print("Conceito B")
elif nota >= 7.5 and nota < 9:
    if faltas <= 20:
        print("Conceito B")
    else:
        print("Conceito C")
elif nota >= 5 and nota < 7.5:
    if faltas <= 20:
        print("Conceito C")
    else:
        print("Conceito D")
elif nota >= 4 and nota < 5:
    if faltas <= 20:
        print("Conceito D")
    else:
        print("Conceito E")
elif nota >= 0 and nota < 4:
    if faltas <= 20:
        print("Conceito E")
    else:
        print("Conceito F")
else:
    print("Nota Invalida")
