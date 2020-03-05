import math as mt 

x=float(input("digite la distancia de la tierra al planeta: "))
v=float(input("digite la velocidad de la nave como fraccion de v: "))

d=x*9.5e15
th=1/(mt.sqrt(1-(v**2)))
c=3e8
t=d/v #unidades de tiempo [s]
n=th*(t-((v*d)/c))

print("el tiempo de la tierra: " ,t, "el tiempo de la nave: " ,n)


