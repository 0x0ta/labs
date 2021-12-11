eng_n = int(input())
eng_n_list = set([])
for each in input().split():
    eng_n_list.add(each)
    
fre_n = int(input())
fre_list = set([])
for each in input().split():
    fre_list.add(each)
    
print(len(eng_n_list.intersection(fre_list)))
