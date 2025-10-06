import os
from config import MAX_CHARS

from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Read the content of the specified file, constrained to the working directory. If the file has more characters than {MAX_CHARS}, it gets truncated at {MAX_CHARS} size.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be read, relative to the working directory.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):

    try:
        file_path = get_file_path(working_directory, file_path)

        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(file_path) > MAX_CHARS:
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