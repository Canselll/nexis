from datetime import datetime, timedelta
from qdrant_client import models
from sentence_transformers import SentenceTransformer
 

config = {
            "POSTGRES": {
                'user': '',
                'password': '',
                'host': '',
                'port': '',
                'dbname': ''
            },

            "DATES": {
                        'end date': datetime(2024, 7, 20),
                        'start date': datetime(2024, 7, 20) - timedelta(days=1)
                    },

            "COLUMNS": ['id', 'flight', 'source_city', 'destination_city','price','departure_date','arrival_date','class','airline'],

            "OPENAI" : {
                        "OPENAI_API_BASE" : 'https://api.groq.com/openai/v1',
                        "OPENAI_MODEL_NAME" : 'llama3-70b-8192' ,
                        "OPENAI_API_KEY" : b'gAAAAABmpz7lcd4njKmau0Y5M0Ganx4qhIakYk_jZ2Hw8ihjhhiGr53jyUma0eL4Sa4FYHJIY3m6TjaNKK1LLVyNlxCeg3niwQA0AoGKPGFY2PtFlHqOvCD0BbiVKbXktUbmoAtKA043MqX0ZOYO14s1hVJOgwrl7Q=='      
                             
                         },

            "QDRANT CLIENT" : {""},

            "ENCODER" : SentenceTransformer('all-MiniLM-L6-v2'),


            "CONNECTION URL" : {""}

        }




