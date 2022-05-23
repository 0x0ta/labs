def reverse_letter(string):
    return "".join(each for each in string[::-1] if each in "abcdefghijklmnopqrstuvwxyz")
