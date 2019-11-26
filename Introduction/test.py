import time

word = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'

def AvgTime() :
    Time = int(input('Enter Your Time To Run : '))
    

def SequencesV1(word) :
    
    totalV1 = 0
    for i in word :
        if i != " " :
            totalV1 += ord(i)
        else :
            pass
    return(totalV1)

print('-'*30)
start = time.time()
print('Answer SequencesV1 : ', SequencesV1(word))
print('Time SequencesV1 : ', (time.time()-start)*1000)
print('-'*30)
