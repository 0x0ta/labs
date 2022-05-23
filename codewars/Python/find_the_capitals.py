def capitals(word):
    return [idx for idx, each in enumerate(word) if each.isupper() is True]
