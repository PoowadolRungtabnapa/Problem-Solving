def Sequential(list_number , Number) :
    step = 0
    index = 0
    for i in list_number :
        if Number == i :
            print(f'{Number} is use {step} step and index is {list_number.index(Number)}.')
            index = 1
        step += 1
    if index != 1 :
        print(f'{Number} not in this list.')
    
list_number = [1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
Number = int(input('Enter Number To Search : '))
Sequential(list_number, Number)