def merge(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j) = (0,0)
    while i+j < m+n:
	if i==m:
	    C.append(B[j])
	    j+=1
	elif j==n:
	    C.append(A[i])
	    i+=1
	elif A[i]<B[j]:
	    C.append(A[i])
	    i+=1
	else:
	    C.append(B[j])
	    j+=1
    return(C)

def mergesort(A,l,r):
    if r-l <=1:
	return(A[l:r])
    if r-l>1 :
	m=(r+l)//2
	L=mergesort(A,l,m)
	R=mergesort(A,m,r)
	return(merge(L,R))

A=range(1,10000,13)
B=range(1,99999,7)
print "A=",A
print "B=",B
C=A+B
print "C=",C
print mergesort(C,0,len(C))


