ListA = [8,12,24,3,16,10,41]
ListB = ['C','B','F','K','Y','Z','G']
ListC = []
A = 0
B = 0
C = 0
D = 0

for i in ListA :
    A += i
    for j in ListB :
        B += ord(j)
        C = i + ord(j)
        D += C
        ListC.append(C)
        ListB.remove(j)
        break

print(f'PrintList C {ListC}')
print(f'SumListA is {A}')
print(f'SumListB is {B}')
print(f'SumListC is {D}')   