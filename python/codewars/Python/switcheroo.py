def switcheroo(s):
    return "".join("b" if each == "a" else "a" if each == "b" else each for each in s)
