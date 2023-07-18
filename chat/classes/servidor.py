import socket

from classes.cryptography_class import My_crypto


class Servidor:
    def __init__(self, host: str, port: int):
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
    

    def start_con(self):
        self.servidor.bind((self.host, self.port))
        self.servidor.listen()

        cliente, end = self.servidor.accept()

        self.start_chat(cliente)

    
    def start_chat(self, cliente):
        terminado = False
        crypto_class = My_crypto()

        while not terminado:
            msg_cifrada = cliente.recv(1024)

            # Descriptografa a mensagem recebida
            msg = crypto_class.decrypt(msg_cifrada.decode('utf-8'))

            if msg == "terminar":
                terminado = True
                print("Chat terminado")
            else:
                print(msg)

            # Criptografa e envia a mensagem de entrada
            mensagem = input('Mensagem: ')
            msg_cifrada = crypto_class.encrypt(mensagem).encode('utf-8')
            cliente.send(msg_cifrada)

        cliente.close()
        self.servidor.close()

