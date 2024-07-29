from .preservice.conclude import Apply

class Serve(Apply):

    def serve(self):

        df = self.apply_data_processing()
        result = self.apply_crew_kick_off(df)

        return result
    