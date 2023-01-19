"""Create a Library class that has a list of books and methods to add and remove books,
search for a book by title, and display all books currently in the library.
"""

import os


class Library:
    all_books = []
    books = 0
    library_path = os.path.join(os.getcwd(), "Books")
    try:
        if os.path.exists(library_path):
            pass
        else:
            os.mkdir(library_path)
        if not os.path.exists(os.path.join(library_path, "Validation.txt")):
            os.rmdir(library_path)
            os.mkdir(library_path)
            with open(os.path.join(library_path, "Validation.txt"), "w") as files:
                files.write("program_open, if you delete me the program\n")
                files.write(
                    "will start from 0 and all of the files will going to be deleted")
        else:
            files = os.listdir(library_path)
            if len(files) != 1:
                books = len(files)-1
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
        self.number = Library.books + 1
        Library.books += 1
        Library.all_books.append(self)

    def __repr__(self) -> str:
        return f"The book {self.name}, are the book #({self.number}),\n Added in the day {self.day} of {self.month},"

    def func_confirmation()->str:
        while True:
            confirmation=input("Are you sure? All of the files will going to be deleted. Y/N: ")
            if confirmation.upper in ["Y","N"]:
                break
        return confirmation
        
    def factory_restart():
        factory_confirmation=Library.func_confirmation()
        if factory_confirmation =="Y":
            os.rmdir(Library.library_path)
            return
        if factory_confirmation == "N":
            return