import re

def data_reverse(data):
    s = []
    r = re.findall("........", "".join(str(each)[::-1] for each in data))
    for each in r[::-1]:
        for c in each:
            s.append(int(c))
    return s
