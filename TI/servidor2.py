import socket
from cryptography.fernet import Fernet

def broadcast(mensaje, sender=None):
<<<<<<< HEAD

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
=======
>>>>>>> 516320a3bfaab35080dcbfb3667a035710b4c79d
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
<<<<<<< HEAD
            cliente.close()
        socketS.close()
=======
            try:
                data = cliente.recv()
                if data:
                    print(f"Mensaje encriptado: {data.decode()}")
                    
                    broadcast(data, cliente)
            except:
                pass
finally:
    for cliente in clientes:
        cliente.close()
    socketS.close()
>>>>>>> 516320a3bfaab35080dcbfb3667a035710b4c79d
