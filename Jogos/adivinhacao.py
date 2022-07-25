import random

print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************")

numero_secreto = random.randint(1, 100)

chute = int(input("Chute um numero de 1 a 100:"))
tentativas = 0

while chute != numero_secreto:
    if chute < numero_secreto: 
        print("O numero que voce chutou e menor!")
        chute = int(input("Chute um novo numero de 1 a 100:"))
        tentativas += 1
    else:
        print("O numero que voce chutou e maior!")
        chute = int(input("Chute um numero de 1 a 100:"))
        tentativas += 1

tentativas += 1
print("Você acertou, o numero era {:d} e precisou de {:d} tentativas para acertar!".format(numero_secreto, tentativas))

print("********Fim de jogo **********")