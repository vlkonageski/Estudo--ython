"""
Leia uma data de nascimento de uma pessoa fornecida atraves de tres numeros inteiro:
Dia, Mes e Ano. Teste a validade desta data para saber se esta é uma data valida. Teste
se o dia fornecido é um dia valido: dia > 0, dia <= 28 para o mes de fevereiro (29 se o ano for bissexto)
dia <=30 em abril, junho, setembro e novembro, dia <=31 nos outros meses. Teste a validade do mes: mes >0 e 
mes <13.Teste a validade do ano: ano <= ano atual (use uma constante definida com o valor igual a 2008). 
Imprimir. "data valida" ou "data invalida" no final da execução do programa.
"""

dia = int(input("Informe o dia:"))
mes = int(input("Informe o mes:"))
ano = int(input("Informe o ano:"))

anoAtual = 2008

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0 and ano <= anoAtual:
    if mes >= 1 and mes <= 12:
        if mes == 2:
            if dia <= 29:
                print("{:d}/{:d}/{:d} Data Valida!".format(dia, mes, ano))
            else:
                print("Data invalida")
        elif mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if dia <= 31:
                print("{:d}/{:d}/{:d} Data Valida!".format(dia, mes, ano))
            else:
                print("Data invalida")
        else:
            if dia <= 30:
                print("{:d}/{:d}/{:d} Data Valida!".format(dia, mes, ano))
            else:
                print("Data invalida")
elif ano <= anoAtual:
    if mes >= 1 and mes <= 12:
        if mes == 2:
            if dia <= 28:
                print("{:d}/{:d}/{:d} Data Valida!".format(dia, mes, ano))
            else:
                print("Data invalida")
        elif mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if dia <= 31:
                print("{:d}/{:d}/{:d} Data Valida!".format(dia, mes, ano))
            else:
                print("Data invalida")
        else:
            if dia <= 30:
                print("{:d}/{:d}/{:d} Data Valida!".format(dia, mes, ano))
            else:
                print("Data invalida")
else:
    print("Data Invalida!")
