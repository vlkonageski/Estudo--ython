import random

print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************")

numero_secreto = random.randint(1, 100)

chute = int(input("Chute um numero de 1 a 100:"))
tentativas = 0

while chute != numero_secreto:
    if chute < 1 or chute > 100:
        print("Voce deve chutar um numero entre 1 e 100!")
        tentativas += 1
        chute = int(input("Chute um novo numero de 1 a 100:"))
    elif chute < numero_secreto: 
        print("O numero que voce chutou e menor!")
        chute = int(input("Chute um novo numero de 1 a 100:"))
        tentativas += 1
    elif chute > numero_secreto:
        print("O numero que voce chutou e maior!")
        chute = int(input("Chute um numero de 1 a 100:"))
        tentativas += 1

tentativas += 1
print("Você acertou, o numero era {} e precisou de {} tentativas para acertar!".format(numero_secreto, tentativas))
print("********Fim de jogo **********")

