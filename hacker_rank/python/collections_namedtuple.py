# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
i = int(input())
h = input()
total = 0
headers = namedtuple('headers', h.split())

for _ in range(i):
    s = tuple(input().split())
    student = headers(s[0], s[1], s[2], s[3])
    total = total + int(student.MARKS)

print(total / i)
