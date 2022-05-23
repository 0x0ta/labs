string = "ThIsisCoNfUsInG"
sub_string = "is"


def count_substring(string, sub_string):
    idx = 0
    for _ in range(len(string)):
        idx = string.index(sub_string[idx + 1:len(string)])
        print(idx)

    #s = string.find(sub_string)
    # return s if s != -1 else 0


print(count_substring(string, sub_string))
