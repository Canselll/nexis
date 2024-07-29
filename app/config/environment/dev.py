import os
from .base import config
from qdrant_client import QdrantClient


config.update({
                "POSTGRES": {
                    'user': 'postgres',
                    'password': b'gAAAAABmp0cEo9pW_0KKEcErjb2t8eSnbMNsU925uq86oyArV53S7DO5LOfZjhyPUznbh6CYBrNoDYyExoeLQ9Hod2p4TM8psQ==',
                    'host': 'postgres',
                    'port': '5432',
                    'dbname': 'postgres'
                },
                
                
                "QDRANT CLIENT": QdrantClient(url="http://eager_cerf:6333")
            })


os.environ["OPENAI_API_BASE"] = config["OPENAI"]["OPENAI_API_BASE"]
os.environ["OPENAI_MODEL_NAME"] = config["OPENAI"]["OPENAI_MODEL_NAME"]


