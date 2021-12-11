eng_n = input()
eng_list = set([])
for each in input().split():
    eng_list.add(each)

fre_n = input()
fre_list = set([])
for each in input().split():
    fre_list.add(each)
    
print(len(eng_list.symmetric_difference(fre_list)))
