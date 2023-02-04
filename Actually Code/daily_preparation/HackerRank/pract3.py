def minion_game(string: str) -> None:
    VOWELS = set(['A', 'E', 'I', 'O', 'U'])
    n = len(string)
    kevin_score = 0
    stuart_score = 0
    for i in range(n):
        if string[i] in VOWELS:
            kevin_score += n - i
        else:
            stuart_score += n - i
    if kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')
    elif stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)
