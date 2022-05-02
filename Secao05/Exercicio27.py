"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
            _____________________
          |  CATEGORIA |IDADE   |
          | ------------------- |
          |Infantil A| 5 a 7    |
          |Infantil B| 8 a 10   |
          |Juvenil A | 11 a 13  |
          |Juvenil B | 14 a 17  |
          |Senior    | > 18 anos|
          |-------------------- |
"""

idade = int(input("Informe a idade do nadador:"))

if idade >= 5 and idade <= 7:
  print("Infantil A")
elif idade >= 8 and idade <= 10:
  print("Infantil B")
elif idade >= 11 and idade <= 13:
  print("Juvenil A")
elif idade >= 14 and idade <= 17:
  print("Juvenil B")
elif idade > 18: 
  print("Senior")
else:
  print("Não se enquadra em nenhuma categoria")
