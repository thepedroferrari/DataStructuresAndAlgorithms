def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # TODO: Write your solution here
    strLen = len(our_string)
    newStr = ""
    for i in range(strLen):
        newStr += our_string[-i - 1]
    return newStr


print(string_reverser("Pedro"))
