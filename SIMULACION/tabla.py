import random
import pandas as pd

def generar_datos(cantidad):
    datos = []
    
    for _ in range(cantidad):
        genero = "MUJER" if random.random() <= 0.4 else "HOMBRE"
        edad = random.randint(17, 23)
        
        if genero == "HOMBRE":
            altura = round(random.gauss(170, 5))  # Distribución normal
            peso = round(random.gauss(65, 8))
        else:
            altura = round(random.gauss(160, 5))
            peso = round(random.gauss(55, 8))

        lentes = "LENTES" if random.random() < 0.6 else "SIN LENTES"

        prob_ojos = random.random()
        if prob_ojos < 0.66:
            ojos = "MARRON OSCURO"
        elif prob_ojos < 0.3:
            ojos = "MARRON CLARO"
        elif prob_ojos <= 0.02:
            ojos = "VERDES"
        else:
            ojos = "AZULES"

        if genero == "HOMBRE":
            estado_civil = "NOVIA" if random.random() < 0.2 else "LIBRE"
        else:
            estado_civil = "NOVIO" if random.random() < 0.2 else "LIBRE"

        datos.append([genero, edad, altura, peso, lentes, ojos, estado_civil])

    columnas = ["GÉNERO", "EDAD", "ALTURA", "PESO", "LENTES", "OJOS", "ESTADO CIVIL"]
    df = pd.DataFrame(datos, columns=columnas)
    
    return df

cantidad = int(input("Ingrese la cantidad de datos a generar: "))
df_generado = generar_datos(cantidad)

nombre_archivo = "datos_generados.xlsx"
df_generado.to_excel(nombre_archivo, index=False, engine="openpyxl")

print(f"Archivo guardado como {nombre_archivo}")
