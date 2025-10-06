import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:
        directory_path = get_dir_path(working_directory, directory)
        directory_list = os.listdir(directory_path)
        list_with_metadata = []
        for item in directory_list:
            item_path = os.path.join(directory_path, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            list_with_metadata.append(f" - {item}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(list_with_metadata)

    except Exception as error:
        return f"Error: {error}"

def get_dir_path(working_directory, directory="."):

    pwd_absolute_path = os.path.abspath(working_directory)
    dir_absolute_path = os.path.abspath(os.path.join(working_directory, directory))
    
    if not dir_absolute_path.startswith(pwd_absolute_path):
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if not os.path.isdir(dir_absolute_path):
        raise Exception(f'Error: "{directory}" is not a directory')
    
    return dir_absolute_path