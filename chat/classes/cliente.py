import socket

from classes.cryptography_class import My_crypto


class Cliente:
    def __init__(self, host: str, port: int):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port


    def start_con_cliente(self):
        self.cliente.connect((self.host, self.port))

        self.start_chat_cliente()

    
    def start_chat_cliente(self):
        terminado = False
        crypto_class = My_crypto()
        print("Digite 'terminar' para terminar o chat")


        while not terminado:
            mensagem = input("Mensagem: ")

            # Criptografa e envia a mensagem
            msg_cifrada = crypto_class.encrypt(mensagem)
            
            self.cliente.send(msg_cifrada.encode('utf-8'))

            # Recebe e descriptografa a mensagem recebida
            msg_cifrada = self.cliente.recv(1024)
            
            msg = crypto_class.decrypt(msg_cifrada).decode('utf-8')

            if msg == 'terminar': 
                terminado = True
            else:
                print(msg)

        self.cliente.close()