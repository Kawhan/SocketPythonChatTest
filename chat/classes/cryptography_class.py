class My_crypto:
    def __init__(self, key):
        self.key = key

    def encrypt(self, string_verdadeira, conjunto, vezes):
        string_criptografada = ""

        i = 0
        while i < len(string_verdadeira):
            if string_verdadeira[i:i+conjunto]:
                string_invertida = string_verdadeira[i:i+conjunto][::-1]
                string_criptografada += string_invertida
                i += 2
                vezes -= 1
                if vezes == 0:
                    string_criptografada += string_verdadeira[i:]
                    break
            else:
                string_criptografada += string_verdadeira[i]
                i += 1

        string_criptografada = self.second_floor_crypt(string_criptografada)
        return self.third_floor_encrypt(string_criptografada, self.key)

    def second_floor_crypt(self, texto):
        tabela_substituicao = {
            'A': 'El', 'B': 'Fol', 'C': 'Il', 'D': 'Lol', 'E': 'Mel',
            'F': 'Nol', 'G': 'Ol', 'H': 'Pol', 'I': 'Qol', 'J': 'Rel',
            'K': 'Sil', 'L': 'Tel', 'M': 'Ul', 'N': 'Vol', 'O': 'Wol',
            'P': 'Xol', 'Q': 'Yol', 'R': 'Zol', 'S': 'Al', 'T': 'Bl',
            'U': 'Cl', 'V': 'Dl', 'W': 'Eml', 'X': 'Fl', 'Y': 'Gl', 'Z': 'Hl',
            'a': 'el', 'b': 'fol', 'c': 'il', 'd': 'lol', 'e': 'mel',
            'f': 'nol', 'g': 'ol', 'h': 'pol', 'i': 'qol', 'j': 'rel',
            'k': 'sil', 'l': 'tel', 'm': 'ul', 'n': 'vol', 'o': 'wol',
            'p': 'xol', 'q': 'yol', 'r': 'zol', 's': 'al', 't': 'bl',
            'u': 'cl', 'v': 'dl', 'w': 'eml', 'x': 'fl', 'y': 'gl', 'z': 'hl'
        }

        texto_criptografado = ""
        for caractere in texto:
            if caractere in tabela_substituicao:
                texto_criptografado += tabela_substituicao[caractere]
            else:
                texto_criptografado += caractere

        return texto_criptografado

    def third_floor_encrypt(self, msg_decriptograda, key):
        msg_cryptografada = ""
        for i in range(len(msg_decriptograda)):
            char_msg = msg_decriptograda[i]
            char_key = key[i % len(key)]
            msg_cryptografada += chr(ord(char_msg) ^ (char_key))

        print(msg_cryptografada)
        return msg_cryptografada

    def decrypt(self, string_criptografada, conjunto, vezes):
        string_criptografada = self.third_floor_decrypt(
            string_criptografada, self.key)
        string_criptografada = self.second_floor_decrypt(string_criptografada)

        string_descriptografada = ""
        i = 0
        while i < len(string_criptografada):
            if string_criptografada[i:i+conjunto]:
                string_normal = string_criptografada[i:i+conjunto][::-1]
                string_descriptografada += string_normal
                i += 2
                vezes -= 1
                if vezes == 0:
                    string_descriptografada += string_criptografada[i:]
                    break
            else:
                string_descriptografada += string_criptografada[i]
                i += 1
        return string_descriptografada

    def second_floor_decrypt(self, texto_criptografado):
        tabela_substituicao = {
            'A': 'El', 'B': 'Fol', 'C': 'Il', 'D': 'Lol', 'E': 'Mel',
            'F': 'Nol', 'G': 'Ol', 'H': 'Pol', 'I': 'Qol', 'J': 'Rel',
            'K': 'Sil', 'L': 'Tel', 'M': 'Ul', 'N': 'Vol', 'O': 'Wol',
            'P': 'Xol', 'Q': 'Yol', 'R': 'Zol', 'S': 'Al', 'T': 'Bl',
            'U': 'Cl', 'V': 'Dl', 'W': 'Eml', 'X': 'Fl', 'Y': 'Gl', 'Z': 'Hl',
            'a': 'el', 'b': 'fol', 'c': 'il', 'd': 'lol', 'e': 'mel',
            'f': 'nol', 'g': 'ol', 'h': 'pol', 'i': 'qol', 'j': 'rel',
            'k': 'sil', 'l': 'tel', 'm': 'ul', 'n': 'vol', 'o': 'wol',
            'p': 'xol', 'q': 'yol', 'r': 'zol', 's': 'al', 't': 'bl',
            'u': 'cl', 'v': 'dl', 'w': 'eml', 'x': 'fl', 'y': 'gl', 'z': 'hl'
        }

        tabela_substituicao_inversa = {
            valor: chave for chave, valor in tabela_substituicao.items()}

        decrypted_text = ""
        i = 0
        while i < len(texto_criptografado):
            found_match = False
            for tamanho in range(3, 0, -1):
                sequencia = texto_criptografado[i:i + tamanho]
                if sequencia in tabela_substituicao_inversa:
                    decrypted_text += tabela_substituicao_inversa[sequencia]
                    i += tamanho
                    found_match = True
                    break

            if not found_match:
                decrypted_text += texto_criptografado[i]
                i += 1

        return decrypted_text

    def third_floor_decrypt(self, msg_cryptografada, key):
        msg_descriptografada = ""
        for i in range(len(msg_cryptografada)):
            char_msg = ord(msg_cryptografada[i])
            char_key = key[i % len(key)]
            msg_descriptografada += chr((char_msg) ^ (char_key))

        print(msg_descriptografada)
        return msg_descriptografada
