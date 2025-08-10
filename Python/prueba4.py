radio=float(input("ingrese el datos de radio: " ))
altura=float(input("ingrese el datos de altura: " ))

volumen=3.14*((radio)**2)*altura
print("el volumen del cilindro es de: "+ str(volumen),"cm^3")

cond= 300<= volumen

print("se puede llenar con 300 ml de agua?:", cond)