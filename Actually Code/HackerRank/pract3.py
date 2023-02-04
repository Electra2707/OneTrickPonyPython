def minion_game(string):
    pass


if __name__ == '__main__':
    # s = input().upper()
    # assert 0 < len(s) and len(s) <= 10**6
    s = "BANANA"
    VOWELS = set(["A", "E", "I", "O", "U"])
    s_kevin = [s[i:] for i, char in enumerate(s) if char in VOWELS][0]
    s_stuart = [s[i:] for i, char in enumerate(s) if not char in VOWELS][0]


    minion_game(s)
