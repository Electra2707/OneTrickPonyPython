"""Move the first letter of each word to the end of it, then add
"ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text: str) -> str:
    punctuation = ["!", "?", ".", ","]
    list_of_words = text.split()
    new_word = []
    for word in list_of_words:
        if word in punctuation:
            new_word.append(word)
        else:
            word = word[1:]+word[:1]+"ay"
            new_word.append(word)
    return " ".join(new_word)


def pig_it(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())


print(pig_it('O tempora o mores !'))  # ,'igPay atinlay siay oolcay')
print(pig_it('This is my string'))  # ,'hisTay siay ymay tringsay')
