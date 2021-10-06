def well(x):
    if "good" in x and x.count("good") > 2:
        return "I smell a series!"
    elif "bad" in x and "good" not in x:
        return "Fail!"
    else:
        return "Publish!"