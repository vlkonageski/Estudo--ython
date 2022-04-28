"""
A nota final de um estudante é calculada a partir de tres notas atribuidas entre o intervalo de 0 a 10,
respectivamente, a um trabalho de laboratorio, a uma avaliação semestral e a um exame final. 
A media dos três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratorio: 2; 
Avaliação semestral: 3; Exame final: 5; De acordo com o resultado, mostre na tela se o aluno 
esta reprovado (media entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. 
Faça todas as verificações necessarias.
"""

n1 = float(input("Informe a nota do trabalho de laboratorio:"))
n2 = float(input("Informe a nota da avaliação semestral:"))
n3 = float(input("Informe a nota do exame final:"))

media = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

if media >= 0 and media < 3:
    print("A media do aluno foi {:.2f}! Aluno Reprovado!".format(media))
elif media >= 3 and media < 5:
    print("A media do aluno foi {:.2f}! Aluno de Recuperação!".format(media))
else:
    print("A media do aluno foi {:.2f}! Aluno Aprovado!".format(media))
