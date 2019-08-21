fo = open('text.txt','r')
stri =fo.read()
print stri
fo.seek(20,2)
print fo.tell()
fo.close()
print fo.name
