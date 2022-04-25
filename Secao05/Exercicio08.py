"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas sao validas e exiba na tela a media destas notas.
Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota nao possua um valor valido,
este fato deve ser informado ao usuario e o programa termina
"""

n1 = float(input("Informe a primeira nota:"))

if n1 >= 0 and n1 <= 10:
    n2 = float(input("Informe a segunda nota:"))
    if n2 >= 0 and n2 <= 10:
        media = (n1 + n2) / 2
        print("A media do Aluno é {:.2f}!".format(media))
    else:
        print("O valor informado nao é valido!")
else:
    print("O valor informado nao é valido!")
