"""
Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

segundos = int(input("Informe o valor em segundos:"))

horas = int(segundos / 3600)
segundos_rest = segundos % 3600
minutos = int(segundos_rest / 60)
segundos_rest = int(segundos_rest % 60)

print("{} horas, {} minutos e {} segundos".format(horas, minutos, segundos_rest))
