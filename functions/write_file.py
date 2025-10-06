import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content into a given file, constrained to the working directory. If the file or the path to the file doesn't exist, this function creates them. The file path is relative to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path with the file name to be written to. It accepts any file format, so if the file should have any specific format, it must be present at the end of the name of the file",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The file content to be written",
            ),
        },
    ),
)

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