import os

file_size = 10 * 1024 * 1024  # 10MB in bytes
target_size = 2 * 1024 * 1024 * 1024  # 6GB in bytes

output_directory = "files"
os.makedirs(output_directory, exist_ok=True)

while os.path.getsize(output_directory) < target_size:
    file_name = f"file_{os.urandom(4).hex()}.txt"
    file_path = os.path.join(output_directory, file_name)
    
    with open(file_path, "wb") as file:
        file.write(os.urandom(file_size))
    
    print(f"Generated {file_name}")