import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):

    try:
        file_path = get_file_path(working_directory, file_path)

        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string += f"[...File '{file_path}' truncated at 10000 characters]"
        
        return file_content_string
    except Exception as error:
        return f"Error: {error}"

    

def get_file_path(working_directory, file):

    pwd_absolute_path = os.path.abspath(working_directory)
    file_absolute_path = os.path.abspath(os.path.join(working_directory, file))
    
    if not file_absolute_path.startswith(pwd_absolute_path):
        raise Exception(f"Error: Cannot read '{file}' as it is outside the permitted working directory")
    
    if not os.path.isfile(file_absolute_path):
        raise Exception(f"Error: File not found or is not a regular file: '{file}'")
    
    return file_absolute_path