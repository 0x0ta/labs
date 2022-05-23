def vowel_indices(word):
    #    o = []
    #    for idx, each in enumerate(word):
    #        if each.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
    #            o.append(idx+1)
    #    return o

    return [ idx+1 for idx, each in enumerate(word) if each.lower() in 'aeiouy' ]
