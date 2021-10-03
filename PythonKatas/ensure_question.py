def ensure_question(s):
    if s[-1:] != "?":
        s = s + "?"
    return s