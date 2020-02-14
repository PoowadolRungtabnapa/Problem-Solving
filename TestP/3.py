L = ['A','B','C','D','E','F']
a = len(L)
y = 'Y'

J = int(input('Enter Number : '))

while len(L) != 1 :
    I = J - 1
    if a == len(L) :
        while I >= len(L) :
            if I >= len(L) :
                I = I - len(L)
        print(L[I])
        k = L.index(L[I]) 
        L.remove(L[I])
        print(I)
        print(L)
    else :
        if k == 0 :
            pass
        else :
            I = J + k - 1
        while I >= len(L) :
            if I >= len(L) :
                I = I - len(L)
        print(I)
        print(L[I])
        k = L.index(L[I])
        L.remove(L[I])
        print(I)
        print(L)
    