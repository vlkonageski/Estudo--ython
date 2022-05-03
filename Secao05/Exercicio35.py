"""
Leia uma data e determine se ela é valida. Ou seja, verifique se o mes esta entre 1 e 12, e se o dia
existe naquele mes. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos nao bissextos.
"""

dia = int(input("Informe o dia:"))
mes = int(input("Informe o mes:"))
ano = int(input("Informe o ano:"))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
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
else:
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