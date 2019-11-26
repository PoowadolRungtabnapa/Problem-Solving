def read () :
    correct = 'incorrect'
    while correct != 'correct' :
        Principal = int(input('Enter Principal : '))
        Interest = float(input('Enter Interest : '))
        Year = int(input('Enter Number of year : '))
        Time = int(input('Enter Compounding Time : '))
        if Principal > 0 and Interest > 0 and Year > 0 and Time > 0 :
            correct = 'correct'
            Calc(Principal,Interest,Year,Time)
        else :
            print('-'*30)
            print('Number Error')
            print('-'*30)
            correct = 'incorrect'

def Calc (Principal,Interest,Year,Time) :
    Amount = Principal*(1 + Interest/Time)**(Year*Time)
    Print(Amount,Principal,Interest,Year,Time)

def Print (Amount,Principal,Interest,Year,Time) :
    print('-'*30)
    print('Principal is : ',Principal)
    print('Interest is : ',Interest)
    print('Year is : ',Year)
    print('Time is : ',Time)
    print('Amount is : ',int(Amount))
    print('-'*30)

read()