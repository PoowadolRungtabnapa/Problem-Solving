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
        pritn(str(self.data) + ' is found')