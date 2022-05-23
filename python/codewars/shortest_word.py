def find_short(s):
    o = 10000000
    for each in s.split(" "):
        if len(each) < o:
            o = len(each)
    return o
