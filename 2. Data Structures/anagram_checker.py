# Code
def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # TODO: Write your solution here
    dict1 = {}
    dict2 = {}

    for letter in str1.lower():
        if letter == " ":
            continue

        if letter in dict1:
            dict1.update({letter: dict1.get(letter) + 1})
        else:
            dict1.update({letter: 1})

    for letter in str2.lower():
        if letter == " ":
            continue

        if letter in dict2:
            dict2.update({letter: dict2.get(letter) + 1})
        else:
            dict2.update({letter: 1})

    return dict1 == dict2


# print(anagram_checker('water','waiter'))
# print(anagram_checker('Dormitory','Dirty room'))
print(anagram_checker('Slot machines', 'Cash lost in me'))
# print(anagram_checker('A gentleman','Elegant men'))
# print(anagram_checker('Time and tide wait for no man','Notified madman into water'))
