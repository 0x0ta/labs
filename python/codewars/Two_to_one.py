def longest(a1, a2):
    o = ""
    for each in a1 + a2:
        if each not in o:
            o = o + each
    return "".join(sorted(o))
