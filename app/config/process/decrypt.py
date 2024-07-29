from cryptography.fernet import Fernet

class Decrypt():

    def decrypt(self ,key, encrypted_password):
        """
        key: String Format
        encrypted_password: Byte Format
        """
        f = Fernet(key)
        decrypted = f.decrypt(encrypted_password)

        return decrypted.decode()
