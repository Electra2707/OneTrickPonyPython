"""Move the first letter of each word to the end of it, then add
"ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text: str) -> str:
    list_of_words=text.split()
    new_word=[]
    for word in list_of_words:
        word=word[1:]+word[:1]+"ay"
        new_word.append(word)
    return " ".join(new_word)

print(pig_it('Pig latin is cool'))#,'igPay atinlay siay oolcay')
print(pig_it('This is my string'))#,'hisTay siay ymay tringsay')

