def hello(name=""):
    if name != "":
        string = f"Hello, {name[:1].upper()}{name[1::].lower()}!"
    else:
        string = "Hello, World!"
    return string