import os

def get_files_info(working_directory, directory="."):
    pwd_absolute_path = os.path.abspath(working_directory)

    path = os.path.join(working_directory, directory)
    dir_absolute_path = os.path.abspath(path)
    
    if not dir_absolute_path.startswith(pwd_absolute_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        directory_list = os.listdir(path)
        list_with_metadata = []
        for item in directory_list:
            item_path = os.path.join(path, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            list_with_metadata.append(f" - {item}: file_size={file_size} bytes, is_dir={is_dir}")

        files_info = "\n".join(list_with_metadata)

    except Exception as error:
        return f"Error: {error}"

    return files_info
