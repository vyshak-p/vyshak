a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key,a_dict[key])

print a_dict.items() #is in the form of tuple

for k,v in a_dict.items():
    print ("key=%s  value=%s"%(k,v))

for value in a_dict.values():
    print(value)
print a_dict
