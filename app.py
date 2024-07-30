from app.service import Serve

serve = Serve()
result = serve.serve()

# Writing the output to a file
with open("result.txt", "w") as file:
    file.write(result)
