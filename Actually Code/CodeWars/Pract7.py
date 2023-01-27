"""Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter 
words reversed (Just like the name of this Kata). Strings passed
in will consist of only letters and spaces. Spaces will be included
only when more than one word is present.
"""

# def spin_words(sentence:str):
#     list_of_words=sentence.split()
#     return " ".join(x for x in list_of_words if len(x)<=5 x [::-1])

def spin_words(sentence:str):
    list_of_words=sentence.split()
    return " ".join(x [::-1] if len(x)>=5 else x for x in list_of_words )