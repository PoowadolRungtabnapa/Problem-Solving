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
    
    def Deletion(self, dele) :
        if dele == self.data : # ไม่มีตัวเชื่อม
            indexl = 0
            indexr = 0
            if self.left is None :
                indexl = 1
            if self.right is None :
                indexr = 1
            if indexl == 1 and indexr == 1 :
                self.data = None
            else : # มีตัวเชื่อม
                indexl = 0
                indexr = 0
                if self.left is not None :
                    indexl = 1
                if self.right is not None :
                    indexr = 1
                if self.left == 1 or self.right == 1 :
                    self.data = self.left.data
                    self.left.data = None
        elif dele != self.data :
            if dele < self.data :
                if self.left is None :
                    pass
                return self.left.Deletion(dele)
            elif dele > self.data :
                if self.right is None :
                    pass
                return self.right.Deletion(dele)
        
        # ตัวบนสุด
        

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
root.insert(150)
root.insert(120)

root.PrintTree()
print('='*10)
root.Deletion(50)
print('='*10)
root.PrintTree()