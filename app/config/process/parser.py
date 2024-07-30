import argparse
import os
from .decrypt import Decrypt
from ..environment.dev import config

class Parser(Decrypt):
    def parser_config(self):
        parser = argparse.ArgumentParser()

        # Add arguments
        parser.add_argument('--env', type=str, required=True, help='Environment')
        parser.add_argument('--key', type=str, required=True, help='Encrypted key')

        # Parse arguments
        args = parser.parse_args()

        # Get arguments as dictionary
        key = args.key.encode()   # If the key is stored as a byte array, encode
        env = args.env
        
        exec(f"from ..environment.{env} import config" , globals())
          
        # Update config values ​​using encrypted key

        config["POSTGRES"]["password"] = self.decrypt(key ,config["POSTGRES"]["password"])
        os.environ["OPENAI_API_KEY"] = self.decrypt(key ,config["OPENAI"]["OPENAI_API_KEY"])
        
        conn_url = f'postgresql://{config["POSTGRES"]["user"]}:{config["POSTGRES"]["password"]}@{config["POSTGRES"]["host"]}:{config["POSTGRES"]["port"]}/{config["POSTGRES"]["dbname"]}'

        config.update({"CONNECTION URL" : conn_url})
        


        return config
    

parser = Parser()
config = parser.parser_config()

