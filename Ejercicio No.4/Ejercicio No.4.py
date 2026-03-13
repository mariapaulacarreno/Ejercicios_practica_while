# programa para calcular en que rebote la pelota
# no alcanza la quinta parte de la altura inicial

#---------------
# input
#---------------
h = float(input("Ingresela altura inicial: "))

#----------------
# processing
#----------------
limite = h / 5
altura = h
rebote = 0

while altura >= limite:
    altura = altura * 0.9
    rebote = rebote + 1

#---------------
# output
#---------------
print("La pelota no alcanza la quinta parte de la altura inicial en el rebote:", rebote)