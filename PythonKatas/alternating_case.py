def to_alternating_case(string):
    out = ""
    for each in string:
        if each == each.lower():
            out = out + each.upper()
        else:
            out = out + each.lower()
    return out