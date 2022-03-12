class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printtreehelp(self,root):
        if root == None:
        	return
        print(root.data, end = ":")
        if root.left != None:
        	print("L:"+str(root.left.data), end=",")
        if root.right != None:
        	print("R:"+str(root.right.data), end="")
        print()
        self.printtreehelp(root.left)
        self.printtreehelp(root.right)
        
    def printTree(self):
    	self.printtreehelp(self.root)
        
    def searchhelp(self,root,data):
        if root ==None:
            return False
        if root.data == data:
            return True
        if root.data>=data:
            return self.searchhelp(root.left,data)
        else:
            return self.searchhelp(root.right,data)
        
        
    def search(self, data):
        return self.searchhelp(self.root,data)
        
    def inserthelp(self,root,data):
        if root == None:
            node = BinaryTreeNode(data)
            return node
        if root.data>=data:
            root.left = self.inserthelp(root.left,data)
            return root
          
        else:
            root.right = self.inserthelp(root.right,data)
            return root
        
    def insert(self, data):
        self.numNodes = self.numNodes+1
        self.root = self.inserthelp(self.root,data)

        
        
    def min(self,root):
        if root == None:
            return 10000
        if root.left == None:
            return root.data
        return self.min(root.left)
    
    def delhelp(self,root,data):
        if root ==None:
            return False, None
        if root.data<data:
            deleted,nrroot = self.delhelp(root.right,data)
            root.right = nrroot
            return root
        if root.data>data:
            deleted,nlroot = self.delhelp(root.left,data)
            root.left = nlroot
            return root
        if root.left == None and root.right == None:
            return True, None
        if root.left == None:
            return True, root.right
        if root.right == None:
            return True, root.left
        
        replacement =  self.min(root.right)
        root.data = replacement
        deleted,nrroot = self.delhelp(root.right,replacement)
        root.right = nrroot
        return True,root
        
        
    def delete(self, data):
        deleted,nroot = self.delhelp(self.root,data)
        if deleted:
        	self.numNodes=self.numNodes-1
        self.root = nroot
        return deleted
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()
