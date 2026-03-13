# leer los capitales
c1=int(input("capital de pedro"))
c2=int(input("capital de juan"))
c3=int(input("capital necesario para el negocio"))

meses = 0

while (c1+c2) < c3:
    c1 = c1*1.03
    c2 = c2*1.04
    meses +=1

print("podrian realizar el negocio en",meses,meses)