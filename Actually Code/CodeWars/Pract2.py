"""The goal of this exercise is to convert a string to a new string
where each character in the new string is "(" if that character
appears only once in the original string, or ")" if that character
appears more than once in the original string. Ignore capitalization
when determining if a character is a duplicate.
"""


def duplicate_encode(words: str) -> str:
    new_word = ""
    words=words.casefold()
    for i in words:
        count_words = words.count(i)
        if count_words == 1:
            new_word += "("
        else:
            new_word += ")"
    return new_word


#Extemely crompress code
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

print(duplicate_encode("din"))  # , "(((")
print(duplicate_encode("recede"))  # , "()()()")
print(duplicate_encode("Success"))  # ")())())", "should ignore case")
print(duplicate_encode("(( @"))  # , "))((")
