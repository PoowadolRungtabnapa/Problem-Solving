import time
def ABZ():
    global word
    num = 0
    word1 = word.split()
    for i in word1:
        for x in i:
            num += ord(x)
    print(num)
    
word = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
start = time.time()
ABZ()
print("time:",(time.time()-start)*1000)