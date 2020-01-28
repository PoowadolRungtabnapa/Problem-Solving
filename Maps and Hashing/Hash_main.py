import Hash_input
import Hash_search

def main() :
    print(f'<{"="*10}|Choose|{"="*10}>')
    print('1.NewUser')
    print('2.OldUser')
    print('3.Exit')
    c = 'uc'
    while c != 'c' :
        try :
            Choose = int(input('Enter Your Choose : '))
            if 3 >= Choose >= 1 :
                if Choose == 1 :
                    Hash_input()
                if Choose == 2 :
                    Hash_search()
                if Choose == 3 :
                    c = 'c' 
            else :
                print(f'{"-"*10}| Errer |{"-"*10}') 
        except ValueError :
            print(f'{"-"*10}| Errer |{"-"*10}') 
        
main()