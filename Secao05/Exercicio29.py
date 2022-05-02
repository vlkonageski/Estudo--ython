"""
Faça uma prova de matematica para crianças que estao aprendendo a somar numeros inteiro menores
do que 100. Escolha numeros aleatorios entre 1 e 100, e mostre na tela a pergunta:
qual é a soma de A + B, onde A e B sao os numeros aleatorios. Peça a resposta. 
Faça cinco perguntas ao aluno e mostre para ele as perguntas e as respostas corretas,
alem de quantas vezes o aluno acertou.
"""

from random import randint

n = 0
acertos = 0

while (n < 5):
    x = randint(1, 100)
    y = randint(1, 100)
    soma = x + y
    resp = int(input("{:d} + {:d} = ".format(x, y)))
    if soma == resp:
        print("{:d} + {:d} = {:d} Você Acertou!".format(x, y, soma))
        acertos += 1
    else:
        print("{:d} + {:d} = {:d} Você Errou!".format(x, y, soma))
    n += 1

print("Voce acertou {:d} questoes!".format(acertos))
