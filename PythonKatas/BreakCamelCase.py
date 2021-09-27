def solution(s):
    j = 0
    for i, each in enumerate(s):
        if each.upper() == each:
            k = i + j
            s = s[:k] + " " + s[k:]
            j += 1
    return s