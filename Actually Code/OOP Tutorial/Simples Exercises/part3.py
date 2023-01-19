"""Create a Library class that has a list of books and methods to add and remove books,
search for a book by title, and display all books currently in the library.
"""

import os

class Library:
    library_path=os.getcwd()
    if os.path.exists(os.path.join(library_path,"Books")):
        pass
    else:
        os.mkdir(os.path.join(library_path,"Books"))

