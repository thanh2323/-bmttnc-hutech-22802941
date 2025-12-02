import rsa
import os

class RSACipher:
    def __init__(self):
        # Tạo thư mục keys nếu chưa có
        if not os.path.exists('cipher/rsa/keys'):
            os.makedirs('cipher/rsa/keys')

    def generate_keys(self):
        # Tạo cặp khóa 1024 bit
        (public_key, private_key) = rsa.newkeys(1024)
        
        # Lưu Public Key
        with open('cipher/rsa/keys/publicKey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
            
        # Lưu Private Key
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))
        
        return public_key, private_key

    def load_keys(self):
        try:
            with open('cipher/rsa/keys/publicKey.pem', 'rb') as p:
                public_key = rsa.PublicKey.load_pkcs1(p.read())
            with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
                private_key = rsa.PrivateKey.load_pkcs1(p.read())
            return private_key, public_key
        except Exception:
            return None, None

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('utf-8'), key)

    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('utf-8')
        except:
            return "Decryption Failed"

    def sign(self, message, key):
        return rsa.sign(message.encode('utf-8'), key, 'SHA-1')

    def verify(self, message, signature, key):
        try:
            return rsa.verify(message.encode('utf-8'), signature, key) == 'SHA-1'
        except:
            return False