seg=int(input("ingrese la cantidad de segundos: "))

horas=seg//3600
mod1=seg%3600
minutos=mod1//60
mod2=mod1%60

horas =str(horas)
minutos = str(minutos)
mod2 = str(mod2)

print("Horas: " + horas)
print("minutos: " + minutos)
print("segundos: " + mod2)