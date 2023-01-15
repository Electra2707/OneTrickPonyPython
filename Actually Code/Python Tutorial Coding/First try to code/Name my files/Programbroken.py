from fileinput import filenames
import os
FOLDER_PATH = r"C:\\Users\\aleja\\Desktop"


def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in filenames:
        print("File Name:" + fileName)
        print("Folder Path:" + os.path.abspath(os.path.join(dir, fileName)), sep="/n")


if __name__ == "__main__":
    listDir(FOLDER_PATH)
