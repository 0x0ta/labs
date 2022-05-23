def dec_func(text):
    split = int(len(text) / 2)
    o = text[split:]
    e = text[:split]

    final_string = ""

    for i in range(0, split + 1):
        try:
            final_string = final_string + o[i]
        except Exception:
            pass
        try:
            final_string = final_string + e[i]
        except Exception:
            pass

    text = final_string
    return text


def enc_func(text):
    o = ""
    e = ""
    for idx, c in enumerate(text):
        if idx % 2 == 0:
            o = o + c
        else:
            e = e + c
    text = e + o
    return text


def decrypt(text, n):
    if text == "" or n <= 0:
        return text
    else:
        i = 1
        while i <= n:
            text = dec_func(text)
            i += 1
    return text


def encrypt(text, n):
    if text == "" or n <= 0:
        return text
    else:
        i = 1
        while i <= n:
            text = enc_func(text)
            i += 1
    return text
