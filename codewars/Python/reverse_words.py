def reverse_words(text):
    return " ".join(each[::-1] for each in text.split(" "))
