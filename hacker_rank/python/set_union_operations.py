english_n = int(input())
english_nl = set([])
for each in input().split():
    english_nl.add(each)
    
french_n = int(input())
french_nl = set([])
for each in input().split():
    french_nl.add(each)

print(len(english_nl.union(french_nl)))