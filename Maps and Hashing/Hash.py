import random

listKey = [[],[],[],[],[],[],[],[],[],[]]
Hash = [[],[],[],[],[],[],[],[],[],[]]
count = 0

def xHash (Name,Key) : 
    global count
    Number = random.randint(0,9)
    Fr(Number,Key,Name)

def Fr(Number,Key,Name) :
    global listKey
    c = 'uc'
    if listKey[Number] == [] :
        c = 'c'
        listKey[Number] = Key
        Hash[Number] = Name
    if listKey[Number] != [] :
        while c != 'c' :
            Number += 1
            if 10 > Number >= 0 :
                if listKey[Number] == [] :
                    listKey[Number] = Key
                    Hash[Number] = Name
                    c = 'c'
            if Number >= 9 :
                Number = -1
                c = 'uc'

def main() :
    global listKey,count
    
    print('1. Add Number And ID')
    print('2. Search ID')
    print('3. Exit')
    Selection = int(input('Enter Your Number : ')) 
    while Selection != 3 :
        if Selection == 1 :
            if count != 10 :
                count += 1
                Name = input('Enter Name : ')
                Key = int(input('Enter Number : '))
                xHash(Name,Key)
                Selection = int(input('Enter Your Number : ')) 
        if Selection == 2 :
            print(listKey[Hash.index(Name)])
            Selection = int(input('Enter Your Number : ')) 

main()
