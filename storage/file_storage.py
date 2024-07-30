import os

class SaveFile():
    
    def save_result_to_file(self ,result, file_name):
        
        file_path = os.path.join("storage", file_name)

        
        with open(file_path, 'w') as file:
            file.write(result)
        
        print(f"Result saved to {file_path}")

