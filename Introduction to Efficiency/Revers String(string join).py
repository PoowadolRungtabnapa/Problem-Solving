def revers_str_join (s) :
    s1 = ''.join(reversed(s))
    return s1

input_str = 'INE-KMUTNB'
if __name__ =='__main__' :
    print('Revers String using string join =', revers_str_join(input_str))