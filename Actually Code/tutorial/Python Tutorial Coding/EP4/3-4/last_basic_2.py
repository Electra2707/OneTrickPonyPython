"""last_basic_2
Write a Python script to copy all the files in a directory to a new location.
The script should take the source and destination directories as input and copy
all the files from the source to the destination.
"""
import os
from time import sleep


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


def ask_new_dir() -> str:
    """_ask_new_dir_
This function return the destination dir to copy the files,
if it dosen't exits will create a new one
    :return: _main_directory_
    :rtype: str
    """
    while True:
        print("Write the destination directory if do you want a new one just write the name of the directory")
        main_directory = input("Write the destination directory: \n")
        isdir = os.path.isdir(main_directory)
        exist = os.path.exists(main_directory)
        default_dir = os.getcwd()
        if exist is True:
            if not default_dir == main_directory:
                return main_directory
            if default_dir == main_directory:
                print("Lol same dir try again")
                sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
        if exist is False:
            if isdir is True:
                print("Wrong directory")
            default_directory_main=os.path.join(default_dir, main_directory)
            print("The default destination to copy the files is")
            print(default_directory_main)
            print("Do you like it? if you said 'N' you will specify the dir where the file should be created")
            afirmation = input("Y/N: \n")
            if afirmation.upper() == "N":
                os.system("cls" if os.name == "nt" else "clear")
                dire = ask_dir()
                new_dir = os.path.join(dire, main_directory)
                return new_dir
            else:
                return default_directory_main


def ask_continue() -> bool:
    """_ask_continue_
This function confirm is the user want to execute the program,
if the program recipt a negative will cause to stop the script
    :return: _return_
    :rtype: bool
    """
    print("If you said 'N', the program will stop running")
    continuee = input("continue? Y/N: \n")
    if continuee.upper() == "Y":
        return
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("GoodBay")
        raise SystemExit


def main(main1, des):
    """This function is the core of the program,
    it will going to copy the files to the new destination

    :param main1: _the original folders to have the files_
    :type main1: _str_
    :param new_des: _the destination of the copy files_
    :type new1: _str_
    """
    try:
        with open(main1, "rb") as default:
            with open(des, "wb") as new_des:
                new_des.write(default.read())
        print("Files were copied successfully")
    except PermissionError as P:
        print("FAIL", P)
    except FileNotFoundError as F:
        print("Lol no files", F)
    except OSError as E:
        print("FAIL", E)

os.system("cls" if os.name == "nt" else "clear")
print("This program will copy all of the files of a directory to a new one")
MAIN_DIR = ask_dir()
os.system("cls" if os.name == "nt" else "clear")
NEW_DIR = ask_new_dir()
print(f"The files in the directory are {os.listdir(MAIN_DIR)}")
ask_continue()
main(MAIN_DIR,NEW_DIR)
sleep(2)