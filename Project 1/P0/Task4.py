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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Set of possible telemarketers
# Numbers make outgoing calls but do not receive Texts or calls or send texts. In other words,
# some numbers might receive only one of these 3 and would not be considered potential telemarketers.


# Simple hand solution:

# A List of all numbers that make calls.
# B List of all numbers that receive calls
# C List of all numbers that receive texts
# D List of all numbers that send texts

# To be a possible telemarketer, you must be in A, but not B, C, or D.

# Make the lists into a set. In this case if only one of either is met is enough, we don't care for duplicates.
# Loop through A.
# Check if each A is contained in either B, C or D
# If TRUE: Delete the number from the Set
# If FALSE: do nothing and continue.
# We are looking at a quadratic algorithm here.
# When done, sort the Set. sort(set) should be O(n log n)

# Print message
# Loop through A and print each of the remaining numbers one by one.



