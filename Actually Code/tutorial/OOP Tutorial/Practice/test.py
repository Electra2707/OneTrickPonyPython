while True:
    print("Welcome Back to our book managemet system")
    print("-----------------------------------------")
    print("Select an option")
    print("Input 1 for creating a new book")
    print("Input 2 for displaying all of the books")
    print("Input 3 for searching a book for the title")
    print("Input 4 for delete a book")
    print("Input 5 for a factory reset")
    print("Input 6 for exit the program")
    print("-----------------------------------------")
    while True:
        try:
            selection = int(input("Input your selection: "))
            if selection >= 1 and selection <= 6:
                break
            else:
                print("Wrong input ouside the range 1-6")
        except ValueError:
            print("Should be an integral number")
    match selection:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            print("----------------")
            print("Se you next time")
            print("----------------")
            raise SystemExit
