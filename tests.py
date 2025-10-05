from functions.get_file_info import get_file_info
from functions.get_file_content import get_file_content


def test_read_directory():
    result = get_file_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("======================")
    print("")

    result = get_file_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print("======================")
    print("")

    result = get_file_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print("")

    result = get_file_info("calculator", "../")
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



if __name__ == "__main__":
    #test_read_directory()
    test_read_file()