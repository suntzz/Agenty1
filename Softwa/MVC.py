# Vista
class CajasDeMensaje:
    def __init__(self):
        self.titulo = ""

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def solicitar_metros(self, mensaje):
        try:
            return float(input(f"{mensaje}: "))
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
            return self.solicitar_metros(mensaje)

    def mostrar_centimetros(self, mensaje):
        print(f"{self.titulo}\n{mensaje}")

# Modelo
class Convertidor:
    def __init__(self, valor=0.0):
        self.valor = valor

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def convertir_a_centimetros(self):
        return self.valor * 100

# Controlador
class Controladores:
    def __init__(self):
        self.objeto_modelo = Convertidor()
        self.objeto_vista = CajasDeMensaje()

    def iniciar(self):
        self.objeto_vista.set_titulo("Convertir Metros a Centímetros")
        metros = self.objeto_vista.solicitar_metros("Digite la medida en metros")
        self.objeto_modelo.set_valor(metros)
        self.objeto_vista.mostrar_centimetros(f"La medida en centímetros es: {self.objeto_modelo.convertir_a_centimetros()}")

# Programa principal
if __name__ == "__main__":
    objeto_controlador = Controladores()
    objeto_controlador.iniciar()
