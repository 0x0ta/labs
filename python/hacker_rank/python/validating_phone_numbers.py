import re

n = int(input())
for _ in range(n):
    num = input()
    if re.findall("(7|8|9)\d{9}", num) and len(num) == 10:
        print("YES")
    else:
        print("NO")