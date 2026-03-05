import random

vida = 50

print("\033[92mTU VIDA ES DE:\033[0m"+str(vida))

while vida > 0:
    daño = random.randint(5, 15)
    vida = vida - daño

    print("el jefe te quito:", daño, "de vida")
    print("vida restante:", vida)
    if vida < 0:
        print("tu vida llego a 0. perdidte la pelea")
        break