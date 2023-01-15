"""last_basic_1
Write a Python script to search for a specific word or phrase
in all the files in a directory. The script should print the name of the file
and the line number where the word was found.
    :return: _a word/phrase_
    :rtype: _str_
"""

import os
import time


def clear_terminal():
    """
    This function clear the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def ask_dir_word():
    """
    This function ask for one word or phrase and aks for the directory to search for it
    """
    try_clear = False
    while True:
        if try_clear is True:
            time.sleep(2)
        clear_terminal()
        word = input("Write a word or pharse to search: ")
        dir1 = input("Write the directory: ")
        try_clear = True
        if not word.strip() and not os.path.isdir(dir1):
            print("Empty phrase/word and wrong directory")
            print("Try again")
        elif os.path.isdir(dir1) is False:
            print("Wrong directory")
            print("Try again")
        elif os.path.exists(dir1) is False:
            print("The directory dosen't exits")
            print("Try again")
        elif not word.strip():
            print("Empy word")
            print("Try again")
        else:
            clear_terminal()
            return (word, dir1)


WORD, DIRECTORY = ask_dir_word() #Unpacking the strings
FOLDERS = os.listdir(DIRECTORY) 
SUCCESS = False
"""
The success variable work in the way if the code runs properly it don't
do anything but if the code diden't find the work i'll print a mesage or error
"""
COUNTER_FILE = 0
LINE_NUMBER = 0

for folder in FOLDERS:
    """This for loop it's the principal part of the code
    In the list of files assigned before i'll iterrate thorugh them
    searching for the word assinged before and i'll print a message 
    if everytings works as intented
    """    
    file_path = os.path.join(DIRECTORY, folder)
    COUNTER_FILE += 1
    LINE_NUMBER += 1
    try:
        with open(file_path, "r", encoding="utf-8") as carpet:
            contents = carpet.read()
            if WORD in contents:
                print(f"WORD found in file {COUNTER_FILE:*^3}\n{file_path}")
                print(
                    f"The WORD *{WORD}* and the lines in the file: {LINE_NUMBER}\n")
                SUCCESS = True
    except PermissionError as P:
        print(P)
    except UnicodeDecodeError as UD:
        print(UD, folder)

if SUCCESS is False:
    print(
        f"\nNone of the files in the directory have the phrase of word ------{WORD}------\n")
time.sleep(5)
