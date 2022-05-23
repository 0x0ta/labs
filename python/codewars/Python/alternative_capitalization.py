def capitalize(s):
    return ["".join(each.upper() if idx % 2 == 0 else each for idx, each in enumerate(s)), "".join(each.upper() if idx % 2 != 0 else each for idx, each in enumerate(s))]
