# 1.1 
def uniqueChars(string):
    charSet = []
    for c in string:
        if charSet.count(c) >= 1:
            return False
        else:
            charSet.append(c)
    return True

print uniqueChars('test')


# ou
#if string.count(c) > 1:
#    return False
