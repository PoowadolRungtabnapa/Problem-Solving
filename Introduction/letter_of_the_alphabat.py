import time

word = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'

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

def SequencesV2(word) :
    totalV2 = 0
    Letter = {'A':65,'B':66,'C':67,'D':68,'E':69,'F':70
            ,'G':71,'H':72,'I':73,'J':74,'K':75,'L':76    
            ,'M':77,'N':78,'O':79,'P':80,'Q':81,'R':82
            ,'S':83,'T':84,'U':85,'V':86,'W':87,'X':88
            ,'Y':89,'Z':90}
    for i in word :
        if i in Letter :
            totalV2 += Letter[i]
        else :
            pass
    return(totalV2)

start = time.time()
print('Answer SequencesV2 : ', SequencesV2(word))
print('Time SequencesV2 : ', (time.time()-start)*1000)
print('-'*30)

def SequencesV3(word) :
    totalV3 = 0
    for i in word :
        if i == 'A' :
            totalV3 += 65
        if i == 'B' :
            totalV3 += 66
        if i == 'C' :
            totalV3 += 67
        if i == 'D' :
            totalV3 += 68
        if i == 'E' :
            totalV3 += 69
        if i == 'F' :
            totalV3 += 70
        if i == 'G' :
            totalV3 += 71
        if i == 'H' :
            totalV3 += 72
        if i == 'I' :
            totalV3 += 73
        if i == 'J' :
            totalV3 += 74
        if i == 'K' :
            totalV3 += 75
        if i == 'L' :
            totalV3 += 76
        if i == 'M' :
            totalV3 += 77
        if i == 'N' :
            totalV3 += 78
        if i == 'O' :
            totalV3 += 79
        if i == 'P' :
            totalV3 += 80
        if i == 'Q' :
            totalV3 += 81
        if i == 'R' :
            totalV3 += 82
        if i == 'S' :
            totalV3 += 83
        if i == 'T' :
            totalV3 += 84
        if i == 'U' :
            totalV3 += 85
        if i == 'V' :
            totalV3 += 86
        if i == 'W' :
            totalV3 += 87
        if i == 'X' :
            totalV3 += 88
        if i == 'Y' :
            totalV3 += 89
        if i == 'Z' :
            totalV3 += 90
    return(totalV3)

start = time.time()
print('Answer SequencesV3 : ', SequencesV3(word))
print('Time SequencesV3 : ', (time.time()-start)*1000)
print('-'*30)
