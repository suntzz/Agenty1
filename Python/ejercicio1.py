
peso_maximo = float(input("Ingrese el peso máximo soportado por el camión: "))

objetos = []
while True:
    peso = float(input("Ingrese el peso del objeto (o '0' para finalizar): "))
    if peso == 0:
        break
    valor = float(input("Ingrese el valor del objeto: "))
    objetos.append((peso, valor, valor / peso))

objetos.sort(key=lambda x: x[2], reverse=True)

peso_total = 0
valor_total = 0
objetos_seleccionados = []

for obj in objetos:
    if peso_total + obj[0] <= peso_maximo:
        peso_total += obj[0]
        valor_total += obj[1]
        objetos_seleccionados.append((obj[0], obj[1], 1))
    else:
        fraccion = (peso_maximo - peso_total) / obj[0]
        peso_total += obj[0] * fraccion
        valor_total += obj[1] * fraccion
        objetos_seleccionados.append((obj[0] * fraccion, obj[1] * fraccion, fraccion))

print("\nObjetos seleccionados:")
for obj in objetos_seleccionados:
    print("Peso:",obj[0], "Valor:", obj[1], "Fracción:", obj[2])

print("Valor total de la carga:", valor_total)
