from app.service import Serve
from storage.file_storage import SaveFile

serve = Serve()
result = serve.serve()

save_file = SaveFile()
save_file.save_result_to_file(result,'StatusReport.txt')


