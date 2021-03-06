# Code

def string_reverser(our_string):
    new_string = ""

    for i in range(len(our_string)):
        new_string += our_string[(len(our_string) - 1) - i]

    return new_string


def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # TODO: Write your solution here
    wordsArr = our_string.split(" ")
    flippedWords = ""
    for word in wordsArr:
        flippedWords += string_reverser(word) + " "

    return flippedWords.strip()
    pass


print(word_flipper("our string"))
