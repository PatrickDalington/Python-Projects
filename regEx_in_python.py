import re

"""
    RegEx in python  is a sequence of characters
    that forms a search pattern.

    RegEx can be use to check if a string contains
    a particular or specific pattern.
"""

myName = "PatrickDalington"
checker = re.search("^Pat", myName)
print(checker)


# Let us check or search through string for characters
alphabets = "abcdfkqz"
search = re.search("[q]", alphabets)
print(search)
