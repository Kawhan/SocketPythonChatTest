import socket

""" 
O módulo Crypto.Cipher fornece implementações de algoritmos de criptografia simétrica, como o AES (Advanced Encryption Standard). 
Neste caso, estamos importando a classe AES desse módulo, que nos permite criar objetos para criptografar e descriptografar dados usando o algoritmo AES.
"""
from Crypto.Cipher import AES

"""
O módulo Crypto.Util.Padding fornece funções para realizar o preenchimento (padding) dos dados de entrada para que tenham um tamanho compatível com o algoritmo 
de criptografia utilizado. O padding é necessário porque os algoritmos de criptografia normalmente trabalham com blocos de tamanho fixo. 
A função pad permite adicionar o padding necessário a uma mensagem, enquanto a função unpad remove o padding dos dados descriptografados.

"""
from Crypto.Util.Padding import pad, unpad

"""
O módulo Crypto.Random fornece funções para gerar números aleatórios seguros. Neste caso, estamos importando a função get_random_bytes, 
que nos permite gerar uma sequência de bytes aleatórios. Essa função é útil para gerar chaves de criptografia seguras, 
como no exemplo em que usamos get_random_bytes para gerar uma chave de 16 bytes para o algoritmo AES.
"""
import os

from Crypto.Random import get_random_bytes
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('KEY')
key = key[:32]

class Servidor:
    def __init__(self, host: str, port: int):
        # Chave de criptografia. Certifique-se de usar a mesma chave no cliente.py.
        self.chave = key.encode()
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

        # Cria o objeto de criptografia
        cipher = AES.new(self.chave, AES.MODE_ECB)

        while not terminado:
            msg_cifrada = cliente.recv(1024)

            # Descriptografa a mensagem recebida
            msg = unpad(cipher.decrypt(msg_cifrada), AES.block_size).decode('utf-8')

            if msg == "terminar":
                terminado = True
                print("Chat terminado")
            else:
                print(msg)

            # Criptografa e envia a mensagem de entrada
            mensagem = input('Mensagem: ')
            msg_cifrada = cipher.encrypt(pad(mensagem.encode('utf-8'), AES.block_size))
            cliente.send(msg_cifrada)

        cliente.close()
        self.servidor.close()

