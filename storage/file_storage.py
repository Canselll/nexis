import os
from app import result  

class SaveFile():
    
    def save_result_to_file(file_name):
        
        file_path = os.path.join('storage/StatusReport.txt', file_name)
        
        with open(file_path, 'w') as file:
            file.write(result)
        
        print(f"Result saved to {file_path}")


save_file = SaveFile()
save_file.save_result_to_file('result.txt')



