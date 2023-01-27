"""Move the first letter of each word to the end of it, then add
"ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text: str) -> str:
    list_of_words=text.split()
    for word in list_of_words:
        word[:1]
        # short_word=word[:1]
    return short_word
        # "".join()

print(pig_it('Pig latin is cool'))#,'igPay atinlay siay oolcay')
print(pig_it('This is my string'))#,'hisTay siay ymay tringsay')

