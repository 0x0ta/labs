def get_count(sentence):
    c = 0
    for each in sentence:
        if each.lower() in ('a', 'e', 'i', 'o', 'u'):
            c += 1
    return c
