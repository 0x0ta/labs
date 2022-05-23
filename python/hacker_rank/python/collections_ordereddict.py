# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
i = int(input())
a = []
d = {}

a = (input() for _ in range(i))

for each in a:
    ea = each[::-1].split(" ", 1)
    key = ea[1][::-1]
    value = ea[0][::-1]

    if key not in d:
        d[key] = value
    elif key in d:
        d[key] = int(d.get(key)) + int(value)

print("\n".join(str(each) + " " + str(d.get(each)) for each in OrderedDict(d)))
