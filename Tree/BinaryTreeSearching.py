    
class Node :

    def __init__(self, data):
        
        self.left = None
        self.right = None
        self.data = data

# Insert
    def insert(self,data) :
        if self.data :
            if data < self.data :
                if self.left is None :
                    self.left = Node(data)
                else :
                    self.left.insert(data)
            elif data > self.data :
                if self.right is None :
                    self.right = Node(data)
                else :
                    self.right.insert(data)
        else :
            self.data = data
# Search            
    def findval(self, lkpval) :
            if lkpval < self.data :
                if self.left is None :
                    return str(lkpval) + " Not Found"
                return self.left.findval(lkpval)
            elif lkpval > self.data :
                if self.right is None :
                    return str(lkpval) + " Not Found"
                return self.right.findval(lkpval)
            else :
                print(str(self.data) + ' is found')

    def PrintTree(self) :
        if self.left :
            self.left.PrintTree()
        print(self.data),
        if self.right :
            self.right.PrintTree()

# Head
root = Node(25)
# Insert
for i in range (0,51) :
    root.insert(i)
# Searching
root.findval(50)
# PrintAllTree
#root.PrintTree()
