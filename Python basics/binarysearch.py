def bs (arr, l, r, x):  
    if r >= l: 
  
        mid = l + (r - l)/2

        if arr[mid] == x: 
            return mid 

        elif arr[mid] > x: 
            return bs(arr, l, mid-1, x) 
  
        else: 
            return bs(arr, mid+1, r, x) 
  
    else: 
        return -1
  
arr = range(0,100,2) 
x = 10
  
result = bs(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at %d" % result 
else: 
    print "Element is not present in array"
