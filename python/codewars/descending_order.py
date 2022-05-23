def descending_order(num):
    return int("".join(each for each in sorted(str(num))[::-1]))
