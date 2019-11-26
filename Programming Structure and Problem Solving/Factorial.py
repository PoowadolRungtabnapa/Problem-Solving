def Factorail(N) :
    if N > 1 :
        F = N * Factorail(N - 1)
    else :
        F = 1
    return(F)

def main() :
    print('-'*50)
    N = int(input('Enter Your Factorail Number : '))
    print('-'*50)
    F = Factorail(N)
    print(F)

main()
