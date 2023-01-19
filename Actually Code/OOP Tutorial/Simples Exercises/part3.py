"""Create a Library class that has a list of books and methods to add and remove books,
search for a book by title, and display all books currently in the library.
"""

import os


class Library:
    try:
        library_path = os.getcwd()
        validation = False
        if os.path.exists(os.path.join(library_path, "Books")):
            library_path = os.path.join(library_path, "Books")
        else:
            os.mkdir(os.path.join(library_path, "Books"))

        with open(os.path.join(library_path, "Validation.txt"), "w") as files:

            file = files.read()
            if file.startswith("New"):
                validation = True
            else:
                files.writelines(1, "Old")
                validation = False
            files.write("F")
            validation = True
    except PermissionError as P:
        print(P)
        raise SystemExit
    except FileNotFoundError as F:
        print(F)
        raise SystemExit
