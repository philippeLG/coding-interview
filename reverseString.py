# 1.2
def reverseString(string):
    n = len(string)
    new_list = range(n)
    for c in string:
        n -= 1
        new_list[n] = c
    return ''.join(new_list)

print reverseString('test')


# ou
# def reverse(string):
#     """Reverse a given string."""
#     return string[::-1]
