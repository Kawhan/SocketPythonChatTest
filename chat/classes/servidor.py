import hashlib
import pickle
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
        crypto_class = My_crypto(key=b'TESTECGAVESEG URA123')

        while not terminado:
            # Recebe o dado enviado pelo cliente serializado
            data_serialized_received = cliente.recv(1024)

            if not data_serialized_received:
                print("Conexão encerrada.")
                break

            # Deserializa os dados
            data_received = pickle.loads(data_serialized_received)

            # b'terminar' é a representação em bytes da string 'terminar'.
            if data_received.get('mensagem_criptografada') == b'terminar':
                print("Chat terminado pelo cliente.")
                break

            # Recupera as informações e salva cada 1 em uma variável
            msg_cifrada = data_received['mensagem_criptografada']
            hash_received = data_received['hash_original']

            # Descriptografa a mensagem recebida
            msg = crypto_class.decrypt(msg_cifrada.decode('utf-8'), 2, 3)

            # Calcula o hash da mensagem original
            hash_original = hashlib.sha256(msg.encode()).hexdigest()

            # Verifica se teve alteração no hash
            if hash_original == hash_received:
                print("Mensagem recebida sem alterações:", msg)
            else:
                print("A mensagem foi alterada durante a transmissão!")

            # verifica se o chat está encerrado
            if msg == "terminar":
                terminado = True
                print("Chat terminado")
            else:
                print(msg)

            mensagem = input('Mensagem: ')

            # Calcula um hash da mensagem original
            hash_original = hashlib.sha256(mensagem.encode()).hexdigest()

            # Cifra a mensagem
            msg_cifrada = crypto_class.encrypt(mensagem, 2, 3)

            # Cria o objeto com hash original e a mensagem cryptografada
            data = {
                'mensagem_criptografada': msg_cifrada.encode('utf-8'),
                'hash_original': hash_original
            }

            # Seriaaliza os dados
            data_serialized = pickle.dumps(data)

            # Envia os dados
            cliente.send(data_serialized)

        cliente.close()
        self.servidor.close()
