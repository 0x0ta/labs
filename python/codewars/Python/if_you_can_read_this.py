def to_nato(words):
    return " ".join(NATO.get(each.upper()) if each.upper() in NATO else each for each in words.replace(" ", ""))
