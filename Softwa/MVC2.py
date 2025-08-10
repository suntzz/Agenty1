import tkinter as tk
from tkinter import simpledialog, messagebox

# Modelo (Operación)
class Operacion:
    def __init__(self, primero=0.0, segundo=0.0):
        self.primero = primero
        self.segundo = segundo
    
    def set_primero(self, primero):
        self.primero = primero
    
    def set_segundo(self, segundo):
        self.segundo = segundo
    
    def multiplicacion(self):
        return self.primero * self.segundo

# Vista (Mensajes)
class Mensajes:
    def __init__(self):
        self.titulo = ""
    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def solicitar_numero(self, mensaje):
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana principal
        while True:
            valor = simpledialog.askstring(self.titulo, mensaje)
            if valor is None:
                return None  # Si el usuario cancela
            try:
                return float(valor)
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido")
    
    def mostrar_operacion(self, mensaje):
        messagebox.showinfo(self.titulo, mensaje)

# Controlador
class ControladorOperacion:
    def __init__(self):
        self.objeto_modelo = Operacion()
        self.objeto_vista = Mensajes()
    
    def iniciar(self):
        self.objeto_vista.set_titulo("Producto de dos números")
        primero = self.objeto_vista.solicitar_numero("Digite el primer número")
        if primero is None:
            return
        segundo = self.objeto_vista.solicitar_numero("Digite el segundo número")
        if segundo is None:
            return
        self.objeto_modelo.set_primero(primero)
        self.objeto_modelo.set_segundo(segundo)
        resultado = self.objeto_modelo.multiplicacion()
        self.objeto_vista.mostrar_operacion(f"El producto es: {resultado}")

# Programa principal
if __name__ == "__main__":
    objeto_controlador = ControladorOperacion()
    objeto_controlador.iniciar()
