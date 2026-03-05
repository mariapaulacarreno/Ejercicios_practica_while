import random

numero = random.randint(1, 100)
intento = 0

while intento != numero:
    intento = int(input("adivina el numero entre 1 y 100: "))

    if intento < numero:
        print("mas alto")
    elif intento > numero:
        print("mas bajo")

print("adivinaste el numero")