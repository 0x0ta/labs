def rot13(message):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = ""
    for each in message:
        if each not in lower_alphabet and each not in upper_alphabet:
            out = out + each
        elif each.isupper() is True:
            idx = upper_alphabet.index(each)
            chr = upper_alphabet[(idx + 13) % 26]
            out = out + chr
        elif each.isupper() is not True:
            idx = lower_alphabet.index(each)
            chr = lower_alphabet[(idx + 13) % 26]
            out = out + chr
    return out
