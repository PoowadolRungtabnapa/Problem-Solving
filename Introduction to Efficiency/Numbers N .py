import time

def addUpToV1(n) :
    total = 0
    for i in range (n) :
        total += (i + 1)
    return(total)

def addUpToV2(n) :
    return n * (n+1)/2

n = int(input('Input Value : '))

strat = time.time()
print('Answer V1 :', addUpToV1(n))
print('Time V1 :', (time.time()-strat)*1000)

strat = time.time()
print('Answer V2 :', addUpToV2(n))
print('Time V2 :',(time.time()-strat)*1000)