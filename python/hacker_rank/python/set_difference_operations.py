eng_students_n = int(input())
eng_students_list = set([])
for each in input().split():
    eng_students_list.add(each)
    
fre_students_n = int(input())
fre_students_list = set([])
for each in input().split():
    fre_students_list.add(each)
    
print(len(eng_students_list.difference(fre_students_list)))