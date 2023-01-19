"""Create a Library class that has a list of books and methods to add and remove books,
search for a book by title, and display all books currently in the library.
"""

import os
from shutil import rmtree
import datetime


class Library:
    all_books = []
    books = 0
    library_path = os.path.join(os.getcwd(), "Books")
    clean_start = False
    try:
        if os.path.exists(library_path):
            pass
        else:
            os.mkdir(library_path)
            clean_start = True
        if not os.path.exists(os.path.join(library_path, "Validation.txt")):
            rmtree(library_path)
            os.mkdir(library_path)
            with open(os.path.join(library_path, "Validation.txt"), "w") as files:
                files.write("program_open, if you delete me the program\n")
                files.write(
                    "will start from 0 and all of the files will going to be deleted")
            clean_start = True
        else:
            files = os.listdir(library_path)
            if len(files) != 1:
                books = len(files)-1
            clean_start = False
    except PermissionError as P:
        print(P)
        raise SystemExit
    except FileNotFoundError as F:
        print(F)
        raise SystemExit

    def __init__(self, name: str, day: int, month: str) -> None:
        self.name = name
        self.day = day
        self.month = month
        Library.all_books.append(self)

    def __repr__(self) -> str:
        return f"{self.name},{self.day},{self.month}"

    def func_confirmation(self) -> str:
        while True:
            confirmation = input(
                "Are you sure? All of the files will going to be deleted. Y/N: ")
            if confirmation.upper in ["Y", "N"]:
                break
        return confirmation

    def factory_restart(self):
        factory_confirmation = self.func_confirmation()
        if factory_confirmation == "Y":
            rmtree(self.library_path)
            Library.clear_terminal()
            print("Files deleted, goodbay")
            raise SystemExit
        if factory_confirmation == "N":
            return

    def clear_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")

    def append_book_file(self):
        if Library.clean_start:
            with open(os.path.join(Library.library_path, "Repository of books.txt"), "w") as repository:
                repository.write(self.__repr__() + "\n")
        if not Library.clean_start:
            if self not in Library.all_books:
                with open(os.path.join(Library.library_path, "Repository of books.txt"), "a") as repository:
                    repository.write(self.__repr__() + "\n")

    def create_books_from_file():
        if os.path.exists(os.path.join(Library.library_path, "Repository of books.txt")):
            with open(os.path.join(Library.library_path, "Repository of books.txt"), "r", encoding="utf8") as files:
                all_books = files.readlines()
                for book in all_books:
                    book_info = book.strip().split(",")
                    name, day, month = book_info
                    Library(name, day, month)


if Library.clean_start:
    Library.clear_terminal()
    print("Welcome the the book managamet system, please add your first book to our system")
    print("Create your book")
    now = datetime.datetime.now()
    day_month = now.strftime("%d-%m").split("-")
    bookname = input("Write the book name: ")
    bookday, bookmonth = day_month
    while True:
        print("Wrong input try again")
        bookname = input("Write the book name: ")
        if not bookname.strip():
            continue
        elif isinstance(bookname, str):
            break
    book1 = Library(bookname, bookday, bookmonth)
    book1.append_book_file()
if not Library.clean_start:
    Library.create_books_from_file()


while True:
    Library.clear_terminal()
    print("Welcome Back to our book managemet system")
    print("-----------------------------------------")
    print("Select an option")
    print("Input 1 for creating a new book")
    print("Input 2 for displaying all of the books")
    print("Input 3 for searching a book for the title")
    print("Input 4 for delete a book")
    print("Input 5 for a factory reset")
    print("Input 6 for exit the program")
    while True:
        try:
            selection = int(input("Write your selection: "))
            if selection >= 1 and selection <= 6:
                break
            else:
                print("Wrong input ouside the range 1-6")
        except ValueError:
            print("Should be an integral number")
