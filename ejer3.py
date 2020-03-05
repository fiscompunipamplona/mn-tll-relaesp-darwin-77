import math as mt

r=float(input("digite la coordenada r: "))
th=float(input("digite el angulo: "))

x=r*mt.cos(th)
y=r*mt.sin(th)
print("la coordenada x: ", x, "la coordenada y: ", y)

