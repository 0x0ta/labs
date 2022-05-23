def encode(st):
    d = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    return "".join(d.get(each) if each in d else each for each in st)


def decode(st):
    d = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}
    return "".join(d.get(each) if each in d else each for each in st)
