class My_crypto:
    def __init__(self):
        pass
    
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
                
        return string_criptografada


    def decrypt(self, string_criptografada, conjunto, vezes):
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
