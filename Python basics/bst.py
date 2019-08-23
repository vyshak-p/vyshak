class node:
    def __init__(self,val):
	self.val=val
	self.lc=None
	self.rc=None

    def get(self):
	return(self.val)

    def set(self,val):
	self.val=val

    def getchildren(self):
	C=[]
	if(self.lc!=None):
	    C.append(self.lc)
	if(self.rc!=None):
	    C.append(self.rc)
	return C

class bst:
    def __init__(self):
	self.root=None

    def setroot(self,val):
	self.root= node(val)

    def insert(self,val):
	if(self.root is None):
	    self.setroot(val)
	else:
	    self.insertnode(self.root,val)

    def insetnode(self,cnode,val):
	if val<=cnode.val:
	    if cnode.lc is None:
		cnode.lc=node(val)
	    else:
		self.insertnode(cnode.lc,val)
		
		
	if val>cnode.val:
	    if cnode.rc is None:
		cnode.rc=node(val)
	    else:
		self.insertnode(cnode.rc,val)

    def find(self,val):
	return self.findnode(self.root,val)

    def findnode(self,cnode,val):
	if cnode is None:
	    return False
	elif val==cnode.val:
	    return True
	elif val<cnode.val:
	    return self.findnode(cnode.lc,val)
	else:
	    return self.findnode(cnode.rc,val)
tree = bst()
tree.insert(3)
print tree.root.val

print tree.find(3)
print tree.find(47)

	
