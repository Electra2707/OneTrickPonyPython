"""Create a Library class that has a list of books and methods to add and remove books,
search for a book by title, and display all books currently in the library.
"""

import os
from shutil import rmtree
import datetime
import webbrowser


class Library:
    """
    The Library class represents a collection of books.
    It provides methods to add, remove, search for and
    display books.
    The library's books are stored in a file "Repository
    of books.txt" in the "Books" folder in the current working directory.
    """
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
        """
        Initializes a new book object with the given name, day, month, and direction.
        Also adds the new book to the all_books list.
        """
        self.name = name
        self.day = day
        self.month = month
        self.direction = direction
        Library.all_books.append(self)

    def __repr__(self) -> str:
        """
        Return a string representation of the book object in the format of 'name,day,month,direction'
        """
        return f"{self.name},{self.day},{self.month},{self.direction}"

    def factory_restart():
        """
        Prompts the user to confirm if they want to delete all the files in the library,
        and if confirmed, deletes the library folder and exits the program.
        """
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
        """
        Clears the terminal screen.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def append_book_file(self):
        """
        Writes the book information to the "Repository of books.txt" file.
        """
        if Library.clean_start:
            with open(os.path.join(Library.library_path, "Repository of books.txt"), "w") as repository:
                repository.write(self.__repr__() + "\n")
        if not Library.clean_start:
            with open(os.path.join(Library.library_path, "Repository of books.txt"), "a") as repository:
                repository.write(self.__repr__() + "\n")

    def create_books_from_file():
        """
        Reads the books information from the "Repository of books.txt" file and 
        creates book objects for each book, adding them to the all_books list
        """
        if os.path.exists(os.path.join(Library.library_path, "Repository of books.txt")):
            with open(os.path.join(Library.library_path, "Repository of books.txt"), "r") as files:
                all_books = files.readlines()
                for book in all_books:
                    book_info = book.strip().split(",")
                    name, day, month, direction = book_info
                    Library(name, day, month, direction)

    def remove_book(book_name: str):
        """
        Removes the book object with the given name from the all_books list
        and removes it from the "Repository of books.txt" file.
        """
        for book in Library.all_books:
            if book.name == book_name:
                Library.all_books.remove(book)
                with open(os.path.join(Library.library_path, "Repository of books.txt"), "r") as f:
                    lines = f.readlines()
                with open(os.path.join(Library.library_path, "Repository of books.txt"), "w") as f:
                    for line in lines:
                        if book_name not in line:
                            f.write(line)
                print(
                    f"The book {book_name} has been removed from the library.")
                break
        else:
            print(f"{book_name} not found in the library.")


"""
This section of the code is responsible for creating
a new book and adding it to the library. It is executed
when the program is started for the first time, as
indicated by the Library.clean_start attribute.

The code starts by clearing the terminal screen and
displaying a welcome message for the user. Then,
it creates a new book object by prompting the user
to input the book name, day, month and direction.
The date is obtained using the datetime module and
the book name and direction are obtained by asking
the user to input them.

If the book is the first book added to the library,
it creates the "Repository of books.txt" file and appends
the book's information to it. If the program is not started
for the first time, it attempts to create book objects
by reading the information from the "Repository of books.txt"
file. If an exception occurs, it informs the user and prompts
them to make a factory restart.

The overall goal of this part of the code is to create a new
book and add it to the library. The code also handles cases
where the program is started for the first time and when the
program is not started for the first time.
"""


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
        raise SystemExit

"""
This section of code is the main menu of the program.
It displays a list of options to the user and prompts
them to input their selection. The options include
opening a book, displaying all books, searching for a
book by title, creating a new book, deleting a book,
factory reset, and exiting the program.

The code uses a while loop to continuously display
the menu options to the user until they select the
option to exit the program. Once the user inputs their
selection, the code uses a match statement to match
the selection with the corresponding option.

The case 1 option allows the user to open a book.
The program displays a list of all the books in the
library and prompts the user to select one. The program
then opens the selected book in the appropriate application,
whether it's a file or a URL.

The case 2 option allows the user to display all the books
in the library. The program displays the name, date, month,
and direction of all the books in the library.

The case 3 option allows the user to search for a book
by title. The program prompts the user to input the title
of the book they want to search for and then displays the
information of the book if it's found in the library.

The case 4 option allows the user to create a new book
and add it to the library. The program prompts the user
to input the information of the book and then creates a
new book object and adds it to the library.

The case 5 option allows the user to delete a book from
the library. The program prompts the user to input the
title of the book they want to delete and then removes
the book from the library.

The case 6 option allows the user to factory reset the
library. The program prompts the user for confirmation
and if confirmed, deletes all the books from the library.

The case 7 option allows the user to exit the program.
The program exits when this option is selected.

The overall goal of this part of the code is to provide
the user with a menu of options to interact with the library
and handle the user's selection accordingly.
"""
while True:
    print("-Welcome Back to our book managemet system-")
    print("-------------------------------------------")
    print("-++++++++++++ Select an option +++++++++++-")
    print("-------------------------------------------")
    print("-Input 1 for opening a book               -")
    print("-Input 2 for display all of the books     -")
    print("-Input 3 for search for the name of a book-")
    print("-Input 4 for creating a new book          -")
    print("-Input 5 for delete a book                -")
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
            print("---------------------------------------")
            for book in Library.all_books:
                print(book.name)
            print("---------------------------------------")
            print("Input an empty space to return to the menu")
            while True:
                selection = input("Select a book to open it: ")
                if not type(selection) is str:
                    print("Should be a string")
                else:
                    break
            try:
                for book in Library.all_books:
                    if book.name == selection:
                        temp_direction = book.direction
                        break
                else:
                    raise Exception
                if os.path.isfile(temp_direction):
                    os.startfile(temp_direction)
                    print("Opening file")
                else:
                    webbrowser.open(temp_direction)
                    print("Opening link")
                restart = input("Press any key to continue: ")
                Library.clear_terminal()
            except Exception as E:
                Library.clear_terminal()
                print(E)
                print("The program find an error tring to open the file/url")
                restart = input("Press any key to continue: ")
        case 2:
            # Show all of the books
            Library.clear_terminal()
            print("List of the books: ")
            for book in Library.all_books:
                print("*****************")
                print(book.name)
                print(book.day, end=" ")
                print(book.month)
                print(book.direction)
            print("*****************")
            restart = input("Press any key to continue: ")
            Library.clear_terminal()
        case 3:
            # Search for a book
            Library.clear_terminal()
            print("---------------------------------------")
            print("Searching the book name")
            print("---------------------------------------")
            for book in Library.all_books:
                print(book.name)
            print("---------------------------------------")
            print("Remember the search are case sensitivity")
            print("***Input an empty string to return to the main menu***")
            while True:
                book_finded = False
                temp_book_name = input("Write the name of the book: ")
                if not type(temp_book_name) is str:
                    print("Should be a string")
                elif not temp_book_name.strip():
                    break
                else:
                    for book in Library.all_books:
                        if temp_book_name == book.name:
                            print(book)
                            book_finded = True
                if book_finded is False:
                    print("The program was not able to find your book")
                print("---------------------------------------")
            Library.clear_terminal()
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
            # Delete the book
            Library.clear_terminal()
            print("---------------------------------------")
            for book in Library.all_books:
                print(book.name)
            print("---------------------------------------")
            while True:
                book_name = input("Enter the name of the book to delete: ")
                if not type(book_name) is str:
                    print("The name should be a string")
                elif not book_name.strip():
                    print("The name can't be empty")
                else:
                    break
            Library.remove_book(book_name)
            restart = input("Press any key to continue: ")
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
