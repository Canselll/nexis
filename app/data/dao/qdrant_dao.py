import uuid
from qdrant_client import models
from ...config.process.parser import config

class CreateInQdrant():

    def create_collection(self,collection_name):
        
        config['QDRANT CLIENT'].create_collection(
                                collection_name=collection_name,
                                vectors_config=models.VectorParams(
                                    size=config['ENCODER'].get_sentence_embedding_dimension(),
                                    distance=models.Distance.COSINE
                                )
                            )
        
class LoadIntoQdrant():

    def load_points(self,text,collection_name):
        points = [
                models.PointStruct(
                    id=str(uuid.uuid4()), 
                    vector=config['ENCODER'].encode(text).tolist(),
                    payload={"description": text}
                )
            ]

        config['QDRANT CLIENT'].upload_points(
            collection_name= collection_name,
            points=points,
            batch_size=64,
            parallel=1,
            method=None,
            max_retries=3,
            wait=False
                
                )
        
