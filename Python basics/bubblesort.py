def bubbleSort(list):
    for num in range(1,len(list)):
        for i in range(1,num):
            if list[i-1]<list[i]:
                temp=list[i]
                list[i]=list[i-1]
                list[i-1]=temp


alist= list()
number=raw_input("number of elements")

for i in range(int(number)):
    n=raw_input("no: ")
    alist.append(int(n))

print "the unsorted array"

print alist

bubbleSort(alist);

print "sorted array in desc"

print alist
