import string


def is_pangram(s):
    a = ""
    for each in s:
        if each not in a and each.isalpha() is True:
            a = a + each.lower()
    return True if "".join(each for each in sorted(a)) == "abcdefghijklmnopqrstuvwxyz" else False
