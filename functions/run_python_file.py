import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        parent_path = get_parent_path(working_directory, file_path)
        
        file_absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
        function_and_parameters = ["python3", file_absolute_path]
        for arg in args:
            function_and_parameters.append(arg)

        run_result = subprocess.run(function_and_parameters, timeout=30, capture_output=True, cwd=parent_path, text=True)
        final_string = ""
        if run_result is None:
            return "No output produced."
        if run_result.stdout != "":
            final_string += f"STDOUT: {run_result.stdout}"
        if run_result.stderr != "":
            final_string += f"STDERR: {run_result.stderr}"
        if run_result.returncode != 0:
            final_string += f"Process exited with code {run_result.returncode}"
            
        return final_string
    except Exception as error:
        return f"Error: executing Python file: {error}"


def get_parent_path(working_directory, file):

    pwd_absolute_path = os.path.abspath(working_directory)
    file_absolute_path = os.path.abspath(os.path.join(working_directory, file))
    
    if not file_absolute_path.startswith(pwd_absolute_path):
        raise Exception(f'Error: Cannot execute "{file}" as it is outside the permitted working directory')
    
    if not os.path.exists(file_absolute_path):
        raise Exception(f'Error: File "{file}" not found')
    
    if file[-3:] != ".py":
        raise Exception(f'Error: "{file}" is not a Python file.')

    parent_path = file_absolute_path.split("/")
    parent_path.pop()
    parent_path = "/".join(parent_path)
    
    return parent_path