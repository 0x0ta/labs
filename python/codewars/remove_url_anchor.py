def remove_url_anchor(url):
    o = ""
    for each in url:
        if each != "#":
            o = o + each
        else:
            break
    return o
