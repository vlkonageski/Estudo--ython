import random

print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************")

numero_secreto = random.randint(1, 100)

print("Qual Nivel de dificuldade deseja jogar?\n"
    +"1 - Fácil\n"
    +"2 - Médio\n"
    +"3 - Difícil")

dificuldade = int(input("Informe a dificuldade:"))
tentativas = 0
tentativas_restantes = 1

<<<<<<< HEAD
if dificuldade == 1:
    tentativas = 20
elif dificuldade == 2:
    tentativas = 10
elif dificuldade == 3:
    tentativas = 5
else:
    print("Digite uma opção válida!")

print("Tentiva {} de {}.".format(tentativas_restantes, tentativas))
chute = int(input("Chute um numero de 1 a 100:"))

while tentativas_restantes != tentativas:
    if chute < numero_secreto: 
        tentativas_restantes += 1
=======
while chute != numero_secreto:
    if chute < 1 or chute > 100:
        print("Voce deve chutar um numero entre 1 e 100!")
        tentativas += 1
        chute = int(input("Chute um novo numero de 1 a 100:"))
    elif chute < numero_secreto: 
>>>>>>> d340928e4f6bec57ad16579678118237ab595170
        print("O numero que voce chutou e menor!")
        print("Tentiva {} de {}.".format(tentativas_restantes, tentativas))
        chute = int(input("Chute um novo numero de 1 a 100:"))
<<<<<<< HEAD
    elif chute > numero_secreto:
        tentativas_restantes += 1
        print("O numero que voce chutou e maior!")
        print("Tentiva {} de {}.".format(tentativas_restantes, tentativas))
        chute = int(input("Chute um novo numero de 1 a 100:"))
    elif chute == numero_secreto:
        print("Você acertou, o numero era {:d} e precisou de {:d} tentativas para acertar!".format(numero_secreto, tentativas_restantes))
        print("********Fim de jogo **********")
        break
=======
        tentativas += 1
    elif chute > numero_secreto:
        print("O numero que voce chutou e maior!")
        chute = int(input("Chute um numero de 1 a 100:"))
        tentativas += 1

tentativas += 1
print("Você acertou, o numero era {} e precisou de {} tentativas para acertar!".format(numero_secreto, tentativas))
print("********Fim de jogo **********")

>>>>>>> d340928e4f6bec57ad16579678118237ab595170
