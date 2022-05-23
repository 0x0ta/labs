def disemvowel(string_):
    return "".join(each for each in string_ if each.lower() not in "aeiou")
