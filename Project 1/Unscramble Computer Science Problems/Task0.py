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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# the first record on a list is the list[0] entry
# the last record on a list is the list[length-of-list - 1] entry
# I assume every time you reach into the array it is going to count as one operation,
# eg: texts[0] and text[2] would be two different operations.
# There are two variable declarations, one of which takes the len method and a math operation and two array access
# There is then three array access for the text print, plus five concatenations.
# There are four array access for the calls print, plus eight concatenations.
# also, account for two print operations and the function call itself.
# Totalling in O(27)


def getFirstTextAndLastCall():
    # first_text = texts[0]
    # last_call = calls[len(calls) - 1]
    # print("First record of texts, " + first_text[0] + " texts " + first_text[1] + " at time " + first_text[2])
    # print(
    #     "Last record of calls, " +
    #     last_call[0] +
    #     " calls " +
    #     last_call[1] +
    #     " at time " +
    #     last_call[2] +
    #     " lasting " +
    #     last_call[3] +
    #     " seconds"
    # )

    # Udacity Feedback:
    # Suggestion / Learning: inline print. Interesting!
    print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}.")
    print(f"Last record of calls, {calls[-1][0]} calls {calls[-1][1]} at time {calls[-1][2]}, lasting {calls[-1][3]} seconds.")


getFirstTextAndLastCall()
