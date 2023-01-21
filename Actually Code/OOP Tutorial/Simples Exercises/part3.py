"""Create a Library class that has a list of books and methods to add and remove books,
search for a book by title, and display all books currently in the library.
"""

import os
from shutil import rmtree
import datetime
from time import sleep
import subprocess


class Library:
    all_books = []
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
            clean_start = False
    except PermissionError as P:
        print(P)
        raise SystemExit
    except FileNotFoundError as F:
        print(F)
        raise SystemExit

    def __init__(self, name: str, day: int, month: str, direction: str) -> None:
        self.name = name
        self.day = day
        self.month = month
        self.direction = direction
        Library.all_books.append(self)

    def __repr__(self) -> str:
        return f"{self.name},{self.day},{self.month},{self.direction}"

    def factory_restart():
        while True:
            factory_confirmation = input(
                "Are you sure? All of the files will going to be deleted. Y/N: ")
            factory_confirmation = factory_confirmation.upper()
            if factory_confirmation in ["Y", "N"]:
                break
        if factory_confirmation == "Y":
            rmtree(Library.library_path)
            Library.clear_terminal()
            print("Files deleted, goodbay")
            raise SystemExit
        if factory_confirmation == "N":
            return

    def clear_terminal():
        os.system("cls" if os.name == "nt" else "clear")

    def append_book_file(self):
        if Library.clean_start:
            with open(os.path.join(Library.library_path, "Repository of books.txt"), "w") as repository:
                repository.write(self.__repr__() + "\n")
        if not Library.clean_start:
            with open(os.path.join(Library.library_path, "Repository of books.txt"), "a") as repository:
                repository.write(self.__repr__() + "\n")

    def create_books_from_file():
        if os.path.exists(os.path.join(Library.library_path, "Repository of books.txt")):
            with open(os.path.join(Library.library_path, "Repository of books.txt"), "r", encoding="utf8") as files:
                all_books = files.readlines()
                for book in all_books:
                    book_info = book.strip().split(",")
                    name, day, month, direction = book_info
                    Library(name, day, month, direction)


if Library.clean_start:
    Library.clear_terminal()
    print("Welcome the the book managamet system, please add your first book to our system")
    print("Create your book")
    now = datetime.datetime.now()
    bookday = str(now.strftime("%d"))
    bookmonth = str(now.strftime("%b"))
    while True:
        bookname = input("Write the book name: ")
        if not bookname.strip():
            print("The book name can't be empty")
        elif isinstance(bookname, str):
            break
        print("Wrong input try again")
    print("----------------------------------------------------")
    print("Add the direction to find your book")
    print("The direction can be an url or a file directory")
    print("----------------------------------------------------")
    while True:
        bookdirection = input("Add the direction: ")
        if not type(bookdirection) is str:
            print("Should be a string")
        elif not bookdirection.strip():
            print("Can't be an empty string")
        else:
            break
    book1 = Library(bookname, bookday, bookmonth, bookdirection)
    book1.append_book_file()
if not Library.clean_start:
    Library.clear_terminal()
    try:
        Library.create_books_from_file()
    except Exception as E:
        print(f"The program find an error {E}")
        print("We can fix this issue making a factory restart")
        Library.factory_restart()


while True:
    print("-Welcome Back to our book managemet system-")
    print("-------------------------------------------")
    print("-++++++++++++ Select an option +++++++++++-")
    print("-------------------------------------------")
    print("-Input 1 for opening a book  (Not Integrated)             -")
    print("-Input 2 for display all of the books     -")
    print("-Input 3 for searching a book             -")
    print("-Input 4 for creating a new book          -")
    print("-Input 5 for delete a book(Not Integrated)                -")
    print("-Input 6 for a factory reset              -")
    print("-Input 7 for exit the program             -")
    print("-------------------------------------------")
    while True:
        try:
            selection = int(input("Input your selection: "))
            if selection >= 1 and selection <= 7:
                break
            else:
                print("Wrong input ouside the range 1-6")
        except ValueError:
            print("Should be an integral number")
    match selection:
        case 1:
            # Open the book (Not Integrated)
            Library.clear_terminal()
        case 2:
            # Show all of the books
            print("List of instances: ")
            for book in Library.all_books:
                print(book.name)
                print(book.day, end=" ")
                print(book.month)
                print(book.direction)
            print(Library.all_books)
            Library.clear_terminal()
        case 3:
            # Search for a book
            Library.clear_terminal()
            print("For searching the book name, input 1")
            print("For searching the date created, input 2")
            print("For searching the direction, input 3")
            while True:
                search = int(input("Input your selection: "))
                if search >= 1 and search <= 3:
                    break
                else:
                    print("Wrong input ouside the range 1-3")
            match search:
                case 1:
                    print("Remember the search are case sensitivity")
                case 2:
                    pass
                case 3:
                    pass
            restart = input("Press any key to continue: ")
        case 4:
            # Create a new book
            Library.clear_terminal()
            new_book_in_module = "book" + str(len(Library.all_books))
            now = datetime.datetime.now()
            bookday = str(now.strftime("%d"))
            bookmonth = str(now.strftime("%b"))
            while True:
                bookname = input("Add the name of your book: ")
                if not type(bookname) is str:
                    print("The name should be a string")
                elif not bookname.strip():
                    print("The name can't be empty")
                else:
                    break
            while True:
                bookdirection = input("Add your book url or file direction: ")
                if not type(bookdirection) is str:
                    print("The name should be a string")
                elif not bookdirection.strip():
                    print("The name can't be empty")
                else:
                    break
            new_book_in_module = Library(
                bookname, bookday, bookmonth, bookdirection)
            new_book_in_module.append_book_file()
            print("Book created")
            restart = input("Press any key to continue: ")
            Library.clear_terminal()
        case 5:
            # Delete the book (Not Integrated)
            Library.clear_terminal()
        case 6:
            # Delete all of the files
            Library.factory_restart()
        case 7:
            # End Program
            Library.clear_terminal()
            print("----------------")
            print("Se you next time")
            print("----------------")
            raise SystemExit
