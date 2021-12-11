n = int(input())
lst = tuple(input() for _ in range(n))

output_lst = set([])

for each in lst:
    if each not in output_lst:
        output_lst.add(each)
    
print(f"{len(output_lst)}")
