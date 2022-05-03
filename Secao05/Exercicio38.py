"""
Uma empresa decide dar um aumento aos seus funcionários de acordo com um tabela que considera o salário atual
e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente
maior do que os funcionarios com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário 
irá receber um bonus adicional de salário. Faça um programa que leia:
    º O valor do salario atual do funcionário;
    º O tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final
reajustado, ou uma mensagem caso o funcionário nao tenha direito a nenhum aumento.
           ___________________________________________________________
          | SALARIO ATUAL  | REAJUSTE(%)| TEMPO DE SERVIÇO | COMISSAO |
          |-----------------------------------------------------------|
          |Até 500,00      |     25%    | Abaixo de 1 ano  |Sem Bonus |
          |Até 1000,00     |     20%    | De 1 a 3 anos    |  100,00  |
          |Até 1500,00     |     15%    | De 4 a 6 anos    |  200,00  |
          |Até 2000,00     |     10%    | De 7 a 10 anos   |  300,00  |
          |Acima de 2000,00|Sem reajuste| Mais de 10 anos  |  500,00  |
          |-----------------------------------------------------------|
"""

salarioAtual = float(input("Informe o salario atual do funcionario:"))
tempoServico = int(input("Informe a quantos anos trabalha na empresa:"))

if salarioAtual <= 500:
    if tempoServico < 1:
        reajuste = salarioAtual + (salarioAtual * 0.25)
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 1 and tempoServico <= 3:
        reajuste = salarioAtual + (salarioAtual * 0.25) + 100
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 4 and tempoServico <= 6:
        reajuste = salarioAtual + (salarioAtual * 0.25) + 200
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 7 and tempoServico <= 10:
        reajuste = salarioAtual + (salarioAtual * 0.25) + 300
        print("O novo salario é R${:.2f}".format(reajuste))
    else:
        reajuste = salarioAtual + (salarioAtual * 0.25) + 500
        print("O novo salario é R${:.2f}".format(reajuste))
elif salarioAtual > 500 and salarioAtual <= 1000:
    if tempoServico < 1:
        reajuste = salarioAtual + (salarioAtual * 0.20)
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 1 and tempoServico <= 3:
        reajuste = salarioAtual + (salarioAtual * 0.20) + 100
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 4 and tempoServico <= 6:
        reajuste = salarioAtual + (salarioAtual * 0.20) + 200
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 7 and tempoServico <= 10:
        reajuste = salarioAtual + (salarioAtual * 0.20) + 300
        print("O novo salario é R${:.2f}".format(reajuste))
    else:
        reajuste = salarioAtual + (salarioAtual * 0.20) + 500
        print("O novo salario é R${:.2f}".format(reajuste))
elif salarioAtual > 1000 and salarioAtual <= 1500:
    if tempoServico < 1:
        reajuste = salarioAtual + (salarioAtual * 0.15)
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 1 and tempoServico <= 3:
        reajuste = salarioAtual + (salarioAtual * 0.15) + 100
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 4 and tempoServico <= 6:
        reajuste = salarioAtual + (salarioAtual * 0.15) + 200
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 7 and tempoServico <= 10:
        reajuste = salarioAtual + (salarioAtual * 0.15) + 300
        print("O novo salario é R${:.2f}".format(reajuste))
    else:
        reajuste = salarioAtual + (salarioAtual * 0.15) + 500
        print("O novo salario é R${:.2f}".format(reajuste))
elif salarioAtual > 1500 and salarioAtual <= 2000:
    if tempoServico < 1:
        reajuste = salarioAtual + (salarioAtual * 0.10)
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 1 and tempoServico <= 3:
        reajuste = salarioAtual + (salarioAtual * 0.10) + 100
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 4 and tempoServico <= 6:
        reajuste = salarioAtual + (salarioAtual * 0.10) + 200
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 7 and tempoServico <= 10:
        reajuste = salarioAtual + (salarioAtual * 0.10) + 300
        print("O novo salario é R${:.2f}".format(reajuste))
    else:
        reajuste = salarioAtual + (salarioAtual * 0.10) + 500
        print("O novo salario é R${:.2f}".format(reajuste))
else:
    if tempoServico < 1:
        print("Sem Reajuste")
    elif tempoServico >= 1 and tempoServico <= 3:
        reajuste = salarioAtual + 100
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 4 and tempoServico <= 6:
        reajuste = salarioAtual + 200
        print("O novo salario é R${:.2f}".format(reajuste))
    elif tempoServico >= 7 and tempoServico <= 10:
        reajuste = salarioAtual + 300
        print("O novo salario é R${:.2f}".format(reajuste))
    else:
        reajuste = salarioAtual + 500
        print("O novo salario é R${:.2f}".format(reajuste))
