def high(x):
    o = 0
    s = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for each in x.split(" "):
        w = 0
        for c in each:
            w = w + alphabet.index(c) + 1
        if w > o and w != o:
            o = w
            s = each
    return s
