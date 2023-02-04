def minion_game(string):
    pass


if __name__ == '__main__':
    # s = input().upper()
    # assert 0 < len(s) and len(s) <= 10**6
    s = "BANANA"
    VOWELS = set(["A", "E", "I", "O", "U"])
    s_kevin = ""
    s_stuart = ""
    for i,j in s:
        if i in VOWELS:
            s_kevin += s

    minion_game(s)
