L = ['A','B','C','D','E','F']
lenL = len(L)

count = int(input('Enter Number : '))
for i in range(0,lenL):
    num = count-1
    if lenL == len(L) :
        while num >= len(L):
            if num >= len(L):
                num = num-len(L)
        print(L[num])
        previous = L.index(L[num]) 
        L.pop(num)
    else : 
        if previous == 0 :
            pass
        else :
            I = count +  previous - 1
        while I >= len(L) :
            if I >= len(L) :
                I = I - len(L)
        print(L[I])
        k = L.index(L[I])
        L.remove(L[I])


