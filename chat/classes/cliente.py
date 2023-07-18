import hashlib
import os
import socket

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('KEY')
key = key[:32]

class Cliente:
    def __init__(self, host: str, port: int):
        # Chave de criptografia. Certifique-se de usar a mesma chave no servidor.py.
        self.chave = key.encode()
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port


    def start_con_cliente(self):
        self.cliente.connect((self.host, self.port))

        self.start_chat_cliente()

    
    def start_chat_cliente(self):
        terminado = False
        print("Digite 'terminar' para terminar o chat")

        # Cria o objeto de criptografia
        cipher = AES.new(self.chave, AES.MODE_ECB)

        while not terminado:
            mensagem = input("Mensagem: ")

            # Criptografa e envia a mensagem
            msg_cifrada = cipher.encrypt(pad(mensagem.encode('utf-8'), AES.block_size))
            self.cliente.send(msg_cifrada)

            # Recebe e descriptografa a mensagem recebida
            msg_cifrada = self.cliente.recv(1024)
            msg = unpad(cipher.decrypt(msg_cifrada), AES.block_size).decode('utf-8')

            if msg == 'terminar': 
                terminado = True
            else:
                print(msg)

        self.cliente.close()