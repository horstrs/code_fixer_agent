import os
from config import MAX_CHARS

def write_file(working_directory, file_path, content):

    try:
        file_path = get_file_path(working_directory, file_path)

        with open(file_path, "w") as f:
            f.write(content)
            
            return f"Successfully wrote to '{file_path}' ({len(content)} characters written)"
    except Exception as error:
        return f"Error: {error}"


def get_file_path(working_directory, file):

    pwd_absolute_path = os.path.abspath(working_directory)
    file_absolute_path = os.path.abspath(os.path.join(working_directory, file))
    
    if not file_absolute_path.startswith(pwd_absolute_path):
        raise Exception(f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory")
    
    dir_path = os.path.dirname(file_absolute_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    return file_absolute_path