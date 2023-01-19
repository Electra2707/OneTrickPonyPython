"""Create a Library class that has a list of books and methods to add and remove books,
search for a book by title, and display all books currently in the library.
"""

import os


class Library:
    try:
        library_path = os.path.join(os.getcwd(), "Books")
        validation = True
        if os.path.exists(library_path):
            pass
        else:
            os.mkdir(library_path)
        if not os.path.exists(os.path.join(library_path, "Validation.txt")):
            os.rmdir(library_path)
            os.mkdir(library_path)
            with open(os.path.join(library_path, "Validation.txt"), "w") as files:
                files.write(
                    "new_program_open, if you delete me the program will start from 0 and all of the files will going to be deleted")
                validation = True
        else:
            validation = False
    except PermissionError as P:
        print(P)
        raise SystemExit
    except FileNotFoundError as F:
        print(F)
        raise SystemExit
