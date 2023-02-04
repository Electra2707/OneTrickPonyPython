if __name__ == '__main__':
    n = 20
    if n % 2 == 0: #even
        if n<=5:
            print("Not Weird")
        elif n >= 21:
            print("Not Weird")
        else:
            print("Weird")
    if n % 2 != 0: #odd
        print("Weird")