import random

listKey = [[],[],[],[],[],[],[],[],[],[]]
Hash = [[],[],[],[],[],[],[],[],[],[]]
count = 0

def xHash (Name,Key) : 
    global count
    Number = random.randint(0,9)
    Fr(Number,Key,Name)

def Fr(Number,Key,Name) :
    global listKey,count
    c = 'uc'
    if [] not in listKey :
        print('Full !!!')
        
    else :
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
    print(listKey)

def main() :
    global listKey,count
    
    print('1. Add Name and ID')
    print('2. Search ID')
    print('3. Exit')
    c = 'uc'
    while c != 'c' :    
        Selection = int(input('Enter Your Number : ')) 
        if 3 >= Selection >= 1 :
            c = 'c'
            if Selection == 1 :
                Name = input('Enter Name : ')
                Key = int(input('Enter Number : '))
                xHash(Name,Key)
                print('1. Add Name and ID')
                print('2. Search ID')
                print('3. Exit')
                Selection = int(input('Enter Your Number : ')) 
            if Selection == 2 :
                Name = input('Enter Name : ')
                print(f'Your ID is {listKey[Hash.index(Name)]}')
                print('1. Add Name and ID')
                print('2. Search ID')
                print('3. Exit')
                Selection = int(input('Enter Your Number : ')) 
        else :
            c = 'uc' 
            print('Error Choose')

main()
