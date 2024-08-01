from .preservice.conclude import Apply
from storage.file_storage import SaveFile

class Serve(Apply,SaveFile):

    def serve(self):

        df = self.apply_data_processing()
        result = self.apply_crew_kick_off(df)
        save_file = self.save_result_to_file(result,'StatusReport.txt') 

        return save_file
    
    
