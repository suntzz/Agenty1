def finalizar_compra(productos):
    if not productos:
        return 0, 0  # Evitamos dividir por cero
    total = 0
    for precio in productos:
        if precio < 0:
            print(f"Error: precio negativo detectado ({precio}). Ignorando...")
            continue
        total += precio

    promedio = total / len(productos)
    return total, promedio

lista_productos = [100, 200, 0, -50]
total, promedio = finalizar_compra(lista_productos)
print("Total:", total)
print("Promedio:", promedio)
