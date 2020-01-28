import random as rd
# OFL = OpenFileList

OFL = open('List.txt','r')

Name = input('Enter Your Name : ')
ID = int(input('Enter Your ID : '))

Number  = rd.randint(0,157)

if OFL[Number] == [] :
        c = 'c'     
        OFL[Number] = ID
        Hash[Number] = Name
if OFL[Number] != [] :
    while c != 'c' :
        Number += 1
        if 157 > Number >= 0 :
            if OFL[Number] == [] :
                OFL[Number] = ID
                Hash[Number] = Name
                c = 'c'
        if Number >= 157 :
            Number = -1
            c = 'uc'
