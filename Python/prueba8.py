lista=input("digite cadena de numeros separados por espacios: ")
datos=lista.split()

print(datos)
datos.insert(9,"pollos")
print(datos)

elim=datos.pop()
print(datos)
print(elim)