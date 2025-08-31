import socket
import threading
from cryptography.fernet import Fernet

def recibir_mensajes():

    host = "4.tcp.ngrok.io"
    port = 14022    

    socketC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketC.connect((host, port))

    llave = socketC.recv(44)
    cifrar = Fernet(llave)

    print("Conectado al servidor. Puedes empezar a chatear!")

    while True:
        try:
            dato = socketC.recv(1024)
            if dato:
                mensaje_desencriptado = cifrar.decrypt(dato).decode()
                print(f"\nOtro usuario: {mensaje_desencriptado}")
                print("Tú: ", end="", flush=True)
        except:
            break

    threading.Thread(target=recibir_mensajes, daemon=True).start()

    while True:
        mensaje = input("Tú: ")
        if mensaje.lower() == 'salir':
            break
        
        mensaje_encriptado = cifrar.encrypt(mensaje.encode())
        socketC.send(mensaje_encriptado)

    socketC.close()