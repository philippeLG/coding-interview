# 1.3 Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer. NOTE: One or two additional variables are fine.
# An extra copy of the array is not.
def removeDup(string):
    n = len(string)
    newList = []

    for c in string:
        if newList.count(c) == 0:
            newList.append(c)

    return ''.join(newList)

print removeDup('test')


# ou
# def remove_duplicates(string):
#     """Remove duplicate characters in a string."""
#     return set(string)
