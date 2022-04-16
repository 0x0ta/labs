def is_isogram(string):
    o = ""
    for each in string:
        if each.lower() not in o:
            o = o + each.lower()
            
    return True if o == string.lower() else False