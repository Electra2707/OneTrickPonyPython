def minion_game(string: str, VOWELS: tuple) -> int:
    if string.startswith(VOWELS):
        return 0
    if not string.startswith(VOWELS):
        return 1

if __name__ == '__main__':
    # s = input().upper()
    # assert 0 < len(s) and len(s) <= 10**6
    s = "BANANA"
    VOWELS = set(["A", "E", "I", "O", "U"])
    S_KEVIN = [s[i:] for i, char in enumerate(s) if char in VOWELS][0]
    S_STUART = [s[i:] for i, char in enumerate(s) if not char in VOWELS][0]
    VOWELS = tuple(VOWELS)
    number_kevin = minion_game(S_KEVIN, VOWELS)
    number_stuart = minion_game(S_STUART, VOWELS)
    if number_kevin > number_stuart:
        print(f"Kevin {number_kevin}")
    elif number_stuart > number_kevin:
        print(f"Stuart {number_stuart}")
    else:
        print("Draw")
