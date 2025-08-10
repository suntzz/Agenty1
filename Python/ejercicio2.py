peso_maximo = 520
objetos = [(1, 20, 15), (2, 30, 50), (3, 15, 20), (4, 40, 55), (5, 80, 92)]

peso_total = 0
valor_total = 0
objetos_seleccionados = []

i = 0
while i < len(objetos) and peso_total < peso_maximo:
    obj_id, peso, valor = objetos[i]
    if peso_total + peso <= peso_maximo:
        objetos_seleccionados.append((obj_id, peso, valor))
        peso_total =peso_total+peso
        valor_total = valor_total+valor
    i =i + 1

print("Objetos seleccionados:")
for obj in objetos_seleccionados:
    print("Objeto: ", obj[0] ,"Peso: ", obj[1], "Valor: ", obj[2])

print("\nPeso total de la carga:", peso_total)
print("Valor total de la carga:", valor_total)