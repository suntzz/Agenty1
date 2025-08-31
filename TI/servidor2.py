import socket
from cryptography.fernet import Fernet

def broadcast(mensaje, sender=None):

    llave = Fernet.generate_key()
    cifrar = Fernet(llave)

    HOST = "127.0.0.1"
    PORT = 5000

    socketS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketS.bind((HOST, PORT))
    socketS.listen(2)

    print(f"Servidor escuchando en {HOST}:{PORT}")
    print(f"Clave de encriptación: {llave.decode()}")

    clientes = []

    """Enviar mensaje a todos los clientes excepto al sender"""
    for cliente in clientes:
        if cliente != sender:
            try:
                cliente.send(mensaje)
            except:
                clientes.remove(cliente)

    while len(clientes) < 2:
        conn, addr = socketS.accept()
        clientes.append(conn)
        print(f"Cliente {len(clientes)} conectado desde {addr}")
        conn.send(llave)

    print("Ambos clientes conectados. Chat iniciado...")

    try:
        while True:
            for cliente in clientes:
                try:
                    data = cliente.recv(1024)
                    if data:
                        print(f"Mensaje encriptado: {data.decode()}")
                        
                        broadcast(data, cliente)
                except:
                    pass
    finally:
        for cliente in clientes:
            cliente.close()
        socketS.close()