class My_crypto:
    def __init__(self):
        pass
    
    def encrypt(self, string):
        
        string_invertida = string[::-1]
    
        return string_invertida


    def decrypt(self, string_invertida):
        
        string_original = string_invertida[::-1]
        
        return string_original
