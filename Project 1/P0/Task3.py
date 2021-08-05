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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# Part A:Find all of the area codes and mobile prefixes called by people
# in Bangalore. In other words, the calls were initiated by "(080)" area code
# to the following area codes and mobile prefixes:
#
# If the number is called by someone in Bangalore, it means that the caller prefix is (080).
#
bangalorePrefix = '(080)'
# Now we don't want every caller, we want only callers from Bangalore, so we can filter the others out.
# For this filter, we want to check:
# Look at all call logs
# If the prefix for the phone number set as the caller starts with (080) we want the log
# If not, we want to drop that line.

# This will be O(1)
def identifyCaller(caller):
    """"
    Whenever we look at a number, we want to quickly identify what kind of number it is.
    This function returns what type of caller it is by analyzing the caller number.
    """""

    if caller.startswith("(0"):
        return 'landline'
    if caller.startswith("7") or caller.startswith("8") or caller.startswith("9"):
        if ' ' in caller:
            return 'mobile'
    if caller.startswith("140"):
        return "telemarketer"


allPrefixes = []
landlinePrefixes = []
mobilePrefixes = []
telemarketingPrefixes = []
unknownPrefixes = []

# This will be O(n)
for call in calls:
    # Quickly drop of if call is not from bangalore
    if not call[0].startswith(bangalorePrefix):
        continue

    called = call[1]
    identity = identifyCaller(called)

    # Hydrate the lists with the called number prefix
    if identity == 'landline':
        landlinePrefixes.append(called[0:called.index(')') + 1])
    elif identity == 'mobile':
        mobilePrefixes.append(called[0:called.index(' ')])
    elif identity == 'telemarketer':
        telemarketingPrefixes.append("140")
    else:
        unknownPrefixes.append(called)

# Add all the prefix to the list in chunks. Extend is O(k) according to https://wiki.python.org/moin/TimeComplexity
allPrefixes.extend([*landlinePrefixes, *mobilePrefixes, *telemarketingPrefixes, *unknownPrefixes])

# The list should already be partially ordered since we placed the info in chunks instead of randomly.
# This could potentially speed up the next sorting algorithm. Worst case O(n log n)
sortedPrefixes = sorted(allPrefixes, key=lambda x: x[0])


print("The numbers called by people in Bangalore have codes:")
for prefix in sortedPrefixes:
    print(prefix)


# Part B
# We are going to partially repeat the first step now using the landlinePrefixes list.

totalLandlineCallsFromBangalore = len(landlinePrefixes)
landlineCallsFromBangaloreToBangalore = 0

# This will be O(n), but something tells me I could solve this problem by looking at the first iteration in the sorted
# Array, then start counting, then stop counting at the last iteration.
# Since values are already organised, I could reduce the amount of work by not even trying to loop through data I know
# It is not going to be what I want.
for call in landlinePrefixes:
    if call.startswith(bangalorePrefix):
        landlineCallsFromBangaloreToBangalore += 1

percentageFromBangaloreToBangalore = landlineCallsFromBangaloreToBangalore / totalLandlineCallsFromBangalore * 100
message = "{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."


print(message.format(percentage=percentageFromBangaloreToBangalore))

# Final simplified time complexity:
# O(n)
