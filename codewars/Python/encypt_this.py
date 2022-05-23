def encrypt_this(text):
    a = []
    if text is not "":
        for each in text.split(" "):
            s = ""
            for idx, c in enumerate(each):
                if idx == 0:
                    s = str(ord(c))
                elif idx == 1:
                    s = s + each[len(each) - 1]
                elif idx == len(each) - 1:
                    try:
                        s = s + each[1]
                    except Exception:
                        pass
                else:
                    s = s + each[idx]
            a.append(s)
    return " ".join(each for each in a)
