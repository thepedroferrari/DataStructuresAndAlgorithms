"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# Work through some examples by hand.

# Steps:
# 1. Create new list of uniques:
# 2. Look into every list item, one by one
# 3. Check if the value of the item already exists in the unique list.
# 4. If it does, move next
# 5. If it does not, add the value to the unique list and then move next.
# 6. repeat until all lists are done.

# Simple mechanical solution
# inputs:
# list1 = [0, 1, 1, 2, 3, 3, 5, 5, 7]
# list2 = [1, 3, 5, 7, 9, 9]
# expected output: [0,1,2,3,5,7,9]


# def getListOfUniques(l1, l2):
#     unique_list = []
#     for item in l1:
#         if item not in unique_list:
#             unique_list.append(item)
#
#     for item in l2:
#         if item not in unique_list:
#             unique_list.append(item)
#
#     return unique_list
#
#
# assert getListOfUniques(list1, list2), [0, 1, 2, 3, 5, 7, 19]
#
#
# def test():
#     result = getListOfUniques(list1, list2)
#     if result != [0, 1, 2, 3, 5, 7, 9]:
#         print("Test with data:", list1, list2, "failed")
#     else:
#         print("Test case passed!")
#
# test()


# Develop incrementally and test as you go
# the lists we have are a csv, and we need to first get the values that we need from these lists
# into a new list. 2 lists would be worsts case O(2n) considering both lists of equal maximum length
# the uniqueness may be simpler by transforming the two lists into a set, but then we will also have O(2n) again.
# then getting the length of the set O(1). We could perform the addition to the new list directly from the lists
# itself, since we won't be needing the lists with just the numbers.
# moreover, we need the number of callers and receivers.
#

# Calculating O:
# Input for this function will be n number of arrays.
# for every array, we will iterate n number of times
# every time we iterate, we will perform two comparisons and at most two more operations
# There are two for loops operations, that for this exercise I will count each of them as 1 operation
# we declare one list and print at the end with len operation
# in this scope where we have two arrays to work with, we will have:
# two arrays + n iterations per array + 8 operations at most.
# O(2n + 8).
def getListOfUniqueValuesFromListsOfLists(arrays):
    uniqueValues = []
    for arr in arrays:
        for item in arr:
            if not item[0] in uniqueValues:
                uniqueValues.append(item[0])
            if not item[1] in uniqueValues:
                uniqueValues.append(item[1])
    return "There are " + str(len(uniqueValues)) + " different telephone numbers in the records."


print(getListOfUniqueValuesFromListsOfLists([calls, texts]))
