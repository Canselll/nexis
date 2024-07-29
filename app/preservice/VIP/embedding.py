from ...config.process.parser import config

class Vectorize():

    def vectorize_text(self, collection_name):
        
        query_vector = config['ENCODER'].encode("Flight Duration").tolist()

        vectors = config['QDRANT CLIENT'].search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=3
        )

        text = [vector.payload.get('description', '') for vector in vectors][0]

        return text
        



