"""
Escreva um prgrama que escreva na tela, de 1 a 100, de 1 em 1, 3 vezes. A primeira vez deve usar a estrutura de
repetição FOR, a segunda WHILE, e a terceira DO WHILE.
"""
y = 0
z = 1

for x in range(101):
    print("For: ",x)

while y < 100:
    y += 1
    print("While: ",y)

while True:
    print("Do While: ",z)
    z += 1
    if z > 100:
        break