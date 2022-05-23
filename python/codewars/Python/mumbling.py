def accum(s):
    return "-".join(each.upper() + (each.lower() * idx) for idx, each in enumerate(s))
