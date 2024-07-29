import argparse
import os
from .decrypt import Decrypt
from ..environment.dev import config

class Parser(Decrypt):
    def parser_config(self):
        parser = argparse.ArgumentParser()

        # Argümanları ekle
        parser.add_argument('--env', type=str, required=True, help='Environment')
        parser.add_argument('--key', type=str, required=True, help='Encrypted key')

        # Argümanları parse et
        args = parser.parse_args()

        # Argümanları sözlük olarak al
        key = args.key.encode()  # Eğer anahtar bir byte dizisi olarak saklanıyorsa, encode et
        env = args.env
        
        exec(f"from ..environment.{env} import config" , globals())
          
       # Şifreli anahtar kullanarak config değerlerini güncelle

        config["POSTGRES"]["password"] = self.decrypt(key ,config["POSTGRES"]["password"])
        os.environ["OPENAI_API_KEY"] = self.decrypt(key ,config["OPENAI"]["OPENAI_API_KEY"])
        
        conn_url = f'postgresql://{config["POSTGRES"]["user"]}:{config["POSTGRES"]["password"]}@{config["POSTGRES"]["host"]}:{config["POSTGRES"]["port"]}/{config["POSTGRES"]["dbname"]}'

        config.update({"CONNECTION URL" : conn_url})
        


        return config
    

parser = Parser()
config = parser.parser_config()

