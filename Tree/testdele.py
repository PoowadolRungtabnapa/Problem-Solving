index = 0
class Node :

    def __init__(self, data):
        
        self.left = None
        self.right = None
        self.data = data

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
    
    def DelNode (self, dele) :
        if self.right.left is None :
            self.right.DelNode(dele)
        else :
            self.data = self.right.left.data
            self.right.left.data = ""

    def LoopLeft (self) :
        if self.left is None and self.right is None :
            data = self.data
            self.data = ""
            return data
        else :
            if self.left is not None :
                self.left.LoopLeft()
            else :
                self.right.LoopLeft()

    def Deletion(self, dele) :
        global index
        number = self.data
        if dele == root.data :
           self.DelNode(dele)
        else :
            if dele == self.data and index == 1 :
                if self.left is None and self.right is None :
                    self.data = ""
                else :
                    if self.left is not None :
                        self.data = self.left.LoopLeft()
                    else :
                        self.data = self.right.LoopLeft()
                        print(self.data)
            if dele == self.data and index == 2 :
                if self.left is None and self.right is None :
                    self.data = ""
                else :
                    if self.left is not None :
                        self.data = self.left.LoopLeft()
                    else :
                        self.data = self.right.LoopLeft()
            if self.left is not None and self.data == number :
                if dele < self.data :
                    if index == 0 :
                        index = 1
                    self.left.Deletion(dele)
            if self.right is not None and self.data == number :
                if dele > self.data :
                    if index == 0 :
                        index = 2
                    self.right.Deletion(dele)

    def PrintTree(self) :
        if self.left :
            self.left.PrintTree()
        print(self.data),
        if self.right :
            self.right.PrintTree()

root = Node(100)
root.insert(50)
root.insert(30)
root.insert(60)
root.insert(35)
root.insert(150)
root.insert(120)

root.PrintTree()
print('='*10)
root.Deletion(50)
print('='*10)
root.PrintTree()