# 1.4 Write a method to decide if two strings are anagrams or not.
#
def testAnagram(string1,string2):
    if len(string1) == len(string2):
        for c in string1:
            if string2.count(c) != string1.count(c):
                return False
    else:
        return False
    return True

print testAnagram('test','stet')

# ou
# return sorted(first) == sorted(second)
