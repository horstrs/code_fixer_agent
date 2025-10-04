import unittest
from functions.get_files_info import get_files_info

print("results for current directory:")
print(get_files_info("calculator", "."))

print("results for 'pkg' directory:")
print(get_files_info("calculator", "pkg"))

print("results for '/bin' directory:")
print(get_files_info("calculator", "/bin"))

print("results for '../' directory:")
print(get_files_info("calculator", "../"))
