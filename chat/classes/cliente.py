import hashlib
import pickle
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
        crypto_class = My_crypto(key=b'TESTECGAVESEG URA123')
        print("Digite 'terminar' para terminar o chat")

        while not terminado:
            mensagem = input("Mensagem: ")

            # Cria o hash da mensagem
            hash_original = hashlib.sha256(mensagem.encode()).hexdigest()

            # Criptografa e envia a mensagem
            msg_cifrada = crypto_class.encrypt(mensagem, 2, 3)

            # Cria um objeto com a mensagem criptografada e o hash da mensagem original
            data = {
                'mensagem_criptografada': msg_cifrada.encode('utf-8'),
                'hash_original': hash_original
            }

            # Serializa o dado
            data_serialized = pickle.dumps(data)

            # Envia o dado serializado
            self.cliente.send(data_serialized)

            # Recebe o objeto com a mensagem criptografada e o hash unico
            data_serialized_received = self.cliente.recv(1024)

            # Deserializa o dado recebido
            data_received = pickle.loads(data_serialized_received)

            # Recupera as informações do objeto de maneira separada e salva em uma variável
            msg_cifrada = data_received['mensagem_criptografada']
            hash_received = data_received['hash_original']

            # Decripta a mensagem antes cryptada
            msg = crypto_class.decrypt(msg_cifrada.decode('utf-8'), 2, 3)

            # Calcula o hash da mensagem original
            hash_original = hashlib.sha256(msg.encode()).hexdigest()

            # Verifica se teve uma alteração nesse hash
            if hash_original == hash_received:
                print("Mensagem recebida sem alterações:", msg)
            else:
                print("A mensagem foi alterada durante a transmissão!")

            # Verifica se o chat deve ser encerrado
            if msg == 'terminar':
                terminado = True
                print("Conexão encerrada!")
            else:
                print(msg)

        self.cliente.close()
