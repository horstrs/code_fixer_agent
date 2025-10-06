from functions.get_file_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def test_read_directory():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("======================")
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print("======================")
    print("")

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print("")


def test_read_file():
    result = get_file_content("calculator", "main.py")
    print("Result for current directory:")
    print(result)
    print("======================")
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for current directory:")
    print(result)
    print("======================")
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print("Result for current directory:")
    print(result)
    print("======================")
    print("")

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for current directory:")
    print(result)
    print("======================")
    print("")


def test_write_file():

    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for lorem.txt:")
    print(result)
    print("======================")
    print("")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for new-ish file morelorem.txt:")
    print(result)
    print("======================")
    print("")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for home directory:")
    print(result)
    print("======================")
    print("")


def test_run_python_file():

    result = run_python_file("calculator", "main.py")
    print("Result for running calculator without parameters - should print usage instructions:")
    print(result)
    print("======================")
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for running the calculator - should give a kinda nasty rendered result:")
    print(result)
    print("======================")
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for running calculator test file:")
    print(result)
    print("======================")
    print("")

    result = run_python_file("calculator", "../main.py") 
    print("Result for running the calculator - (this should return an error, as it's outside wd):")
    print(result)
    print("======================")
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for running the calculator - (this should return an error, as file doesn't exist):")
    print(result)
    print("======================")
    print("")

"""
def test_main_file_info():

    result = run_python_file("calculator", "main.py")
    print("Result for running calculator without parameters - should print usage instructions:")
    print(result)
    print("======================")
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for running the calculator - should give a kinda nasty rendered result:")
    print(result)
    print("======================")
    print("")

"what files are in the root?" -> get_files_info({'directory': '.'})
"what files are in the pkg directory?" -> get_files_info({'directory': 'pkg'})
"""


if __name__ == "__main__":
    #test_read_directory()
    #test_read_file()
    #test_write_file()
    test_run_python_file()