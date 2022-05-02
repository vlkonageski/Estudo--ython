"""
Leia a distancia em KM e a quantidade de litros de gasolina consumidos por um carro em um percurso, 
calcule o consumo em KM/L e escreva uma mensagem de acordo com a tabela abaixo
            __________________________________
          |  CONSUMO |(KM/L) |  MENSAGEM       |
          | ---------------------------------- |
          | menor que| 8     | Venda o Carro!  |
          | entre    | 8 e 14| Economico!      |
          | maior que| 14    | Super Economico!|
          |----------------------------------- |
"""

km = float(input("Informe a distancia em KM:"))
l = float(input("Informe q quantidade de litros consumidos no percurso:"))
media = km / l

if media < 8:
  print("Vanda o Carro!")
elif media > 8 and media <= 14:
  print("Economico!")
else:
  print("Super Economico!")
