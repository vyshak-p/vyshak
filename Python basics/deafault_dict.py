from collections import defaultdict

count=defaultdict(int)
name_list="Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in name_list:
    count[names]+=1   #deafault dict allows to avoid key error
print count
