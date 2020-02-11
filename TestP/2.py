L = ['A','B','C','D','E','F']
a = len(L)
y = 'Y'

J = int(input('Enter Number : '))

while len(L) != 1 :
    I = J - 1
    while I >= len(L) :
        if I >= len(L) :
            I = I - len(L)
    if a == len(L) :
        print(L[I])
        k = L.index(L[I]) 
        L.remove(L[I])
        print(I)
        print(L)
    else :
        print(L[I])
        k = L.index(L[I])
        print(k)
        if k == 0 :
            pass
        else :
            k += 1
        while I >= len(L) :
            if I >= len(L) :
                I = I - len(L)
        print(I)
        L.remove(L[I])
        I = I + k
        print(I)
        print(L)
    