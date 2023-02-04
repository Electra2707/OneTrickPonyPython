"""Write a Python script to delete all the files in a directory
that have a specific extension. The script should take the directory
name and the extension as input and delete all the files with that extension.
"""
from time import sleep
import os


def ask_dir() -> str:
    """_ask_dir_
This function return one directory only if the dir exists and is a proper dir
    :return: _main_directory_
    :rtype: str
    """
    while True:
        main_directory = input("Write the directory: \n")
        isdir = os.path.isdir(main_directory)
        exist = os.path.exists(main_directory)
        if exist and isdir:
            return main_directory
        if isdir is False:
            print("The directory is incorrect")
            sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
        if exist is False and isdir is True:
            print("The directory dosen't exits")
            sleep(2)
            os.system("cls" if os.name == "nt" else "clear")


def ask_continue() -> bool:
    """_ask_continue_
This function confirm is the user want to execute the program,
if the program recipt a negative will cause to stop the script
    :return: _return_
    :rtype: bool
    """
    print("The program will delete the files")
    print("If you said 'N', the program will stop running")
    continuee = input("continue? Y/N: ")
    while continuee.upper() not in ["Y", "N"]:
        continuee = input("continue? Y/N: ")
        if continuee.upper() == "Y":
            return
        if continuee.upper() == "N":
            os.system("cls" if os.name == "nt" else "clear")
            print("GoodBay")
            raise SystemExit


def generate_list():
    """This function will goin to create a list of the necesary extensions
    and have the posibilitys to keep adding more extensions if its necesary
    the result is going to be a set for to delete duplicate members
    and can give the option to the user to delete and start from 0

    :return: set(files)
    :rtype: set
    """
    files = []
    afirmation = ""
    first_start = True
    while True:
        if files is None:
            files = []
        if first_start is False:
            sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        extension = input("Write your extension to remove: ")
        if not extension.startswith("."):
            print("Wrong extension, try again")
            print("The extension should start with '.'")
        else:
            files.append(extension)
            print(f"the files extensions selected are{files}")
            print("\n\nD will going to delete the list and star adding from 0")
            afirmation = input(
                "Do you want to add more extensions? Y/N/D: ")
            while afirmation.upper() not in ["Y", "N", "D"]:
                afirmation = input(
                "Do you want to add more extensions? Y/N/D: ")
            if afirmation.upper() == "D":
                files = files.clear()
            if afirmation.upper() == "N":
                print("Tre program will remove duplicate extensions")
                sleep(2)
                return set(files)
            if afirmation.upper() == "Y":
                continue
        first_start=False


os.system("cls" if os.name == "nt" else "clear")
print("This script will delete all of the files with the selected extension")
DIRECTORY = ask_dir()
EXTENSIONS = tuple(generate_list())
FILES = os.listdir(DIRECTORY)
os.system("cls" if os.name == "nt" else "clear")

ask_continue()
for file in FILES:
    if os.path.splitext(file)[1] in EXTENSIONS:
        print(file)
        try:
            os.remove(os.path.join(DIRECTORY, file))
            print("Deleted")
        except PermissionError as P:
            print("Error", P)
        except FileNotFoundError as F:
            print("Error", F)
print("Program has ended")
