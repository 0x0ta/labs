def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return " ".join(str(alphabet.index(each.lower()) + 1) for each in text if each.lower() in alphabet)
