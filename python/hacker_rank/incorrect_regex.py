import re


def is_regex(regex):
    try:
        re.compile(regex)
    except re.error:
        return False
    return True


for i in range(int(input())):
    print(is_regex(input()))
