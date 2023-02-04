def minion_game(string: str) -> int:
    constructor = []
    if string.startswith(VOWELS):
        for i in string:
            if i in VOWELS:
                ap
    else:
        pass
    return len(string)


if __name__ == '__main__':
    # s = input().upper()
    # assert 0 < len(s) and len(s) <= 10**6
    s = "BANANA"
    VOWELS = set(["A", "E", "I", "O", "U"])
    S_KEVIN = [s[i:] for i, char in enumerate(s) if char in VOWELS][0]
    S_STUART = [s[i:] for i, char in enumerate(s) if not char in VOWELS][0]
    VOWELS = tuple(VOWELS)
    number_kevin = minion_game(S_KEVIN)
    number_stuart = minion_game(S_STUART)
    if number_kevin > number_stuart:
        print(f"Kevin {number_kevin}")
    elif number_stuart > number_kevin:
        print(f"Stuart {number_stuart}")
    else:
        print("Draw")
