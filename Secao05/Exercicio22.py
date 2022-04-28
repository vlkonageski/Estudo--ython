"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria sao.
 º Ter pelo menos 65 anos
 º Ou ter trabalhado pelo menos 30 anos
 º Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""

idade = int(input("Informe a idade do trabalhador:"))
tempoServico = int(input("Informe o tempo de serviço do trabalhador:"))

if idade >= 65 or tempoServico >= 30 or idade >= 60 and tempoServico >= 25:
    print("É possivel se aposentar!")
else:
    print("Ainda nao é possivel se aposentar!")
