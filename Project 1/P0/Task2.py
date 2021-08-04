"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Work through some examples by hand.
#
# Since numbers can repeat on the call log, we must be sure to sum all different occurrences and get a proper
# amount for each unique number.
# For this I would need a uniques list similar to the previous task, but now instead of only having the number,
# each number should be a dictionary key.
# The value of this key should be the total amount.
# On a piece of paper I would have:

# Phone 1: 500
# Phone 2: 350
# ...
# Phone N: 999
#
# Then after the entire list is compiled with the correct values, I need to find out which of the numbers has
# the largest number of seconds. Manually I would compare numbers one by one and use something to mark the number
# it is the current largest one. On a program I would use a variable. The comparison would be while iterating through
# the numbers, I check if the time for each number is bigger than the time spent on the saved number (if a > b).
# If not, continue next number. If is, substitute the number with the new largest number.

# Simple mechanical Solution:
# randomCalls = [
#     ['78130 00821', '78298 91466', '01-09-2016 06:01:12', '186'],
#     ['78298 91466', '(022)28952819', '01-09-2016 06:01:59', '2093'],
#     ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975'],
#     ['93427 40118', '(080)33118033', '01-09-2016 06:11:23', '1156'],
#     ['90087 42537', '(080)35121497', '01-09-2016 06:17:26', '573']
# ]
#
#
# def getLongestCallFromCallList(callList):
#     longestCall = 0
#     for call in callList:
#         time = int(call[3])
#         if time > longestCall:
#             longestCall = time
#     return longestCall
#
#
# def test():
#     result = getLongestCallFromCallList(randomCalls)
#     if result != 2093:
#         print("Test with data:", randomCalls, "failed")
#     else:
#         print("Test case passed!")
#
#
# test()
#


def getLongestCallFromCallList(callList):
    if not len(callList[0]) == 4:
        return "Error: argument does not match the type"

    uniqueNumbers = {}
    for call in callList:
        time = int(call[3])
        if call[0] in uniqueNumbers:
            uniqueNumbers[call[0]] += time
        else:
            uniqueNumbers[call[0]] = time

        if call[1] in uniqueNumbers:
            uniqueNumbers[call[1]] += time

        else:
            uniqueNumbers[call[1]] = time

    largestAmount = ['', 0]
    for key, value in uniqueNumbers.items():
        if value > largestAmount[1]:
            largestAmount[0] = key
            largestAmount[1] = value

    return largestAmount[0] + " spent the longest time, " + str(largestAmount[1]) + " seconds, on the phone during September 2016."


print(getLongestCallFromCallList(calls))

# Should fail with message:
# print(getLongestCallFromCallList([[1, 2, 3]]))
# print(getLongestCallFromCallList([]))


