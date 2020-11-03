print()
print('              >>>>>>>>>>>>>>>>>    WELCOME    <<<<<<<<<<<<<<<<<')
print()
print('               Maths Table Generator ( 0 to 99 ), Version 1.0')
print()
print('      >> The Source Code of this software is written by Vivek Kumar. <<')
print('                           GitHub --> vivek07kumar')
print('  --------------------------------------------------------------------------')
print()
done = False
c = False
e = True
while not done :
    done2 = False
    done3 = False
    done1check = False
    done2check = False
    done3check = False
    while done1check == False or done2check == False or done3check == False :
        print('>> Please enter two numbers.')
        while not done2 :
            print()
            x = eval(input('* Enter 1st number : '))
            if type(x) == int :
                done2 = True
                done1check = True
            if type(x) == str :
                print()
                print('                         >>>>  ERROR ! Wrong Input  <<<<')
                print()
                print('>> Input must not be String !')
                done1check = False
            if type(x) == tuple :
                print()
                print('                         >>>>  ERROR ! Wrong Input  <<<<')
                print()
                print('>> Input must not be Tuple !')
                done1check = False
            if type(x) == float :
                x = int(x)
                done2 = True
                done1check = True
        while not done3 :
            print()
            y = eval(input('* Enter 2nd number : '))
            if type(y) == int :
                if y == 0 :
                    y = x
                done3 = True
                done2check = True
            if type(y) == str :
                print()
                print('                         >>>>  ERROR ! Wrong Input  <<<<')
                print()
                print('>> Input must not be String !')
                done2check = False
            if type(y) == tuple :
                print()
                print('                         >>>>  ERROR ! Wrong Input  <<<<')
                print()
                print('>> Input must not be Tuple !')
                done2check = False
            if type(y) == float :
                y = int(y)
                if y == 0 :
                    y = x
                done3 = True
                done2check = True
        if y - x > 10 or x > 99 or y > 99 or x > y or x < 0 or y < 0 :
            print('                         >>>>  ERROR ! Wrong Input  <<<<')
            print()
            print('>>  1. Difference between both numbers must be <= 10.')
            print('>>  2. Both the numbers must be >= 0 and < 100.')
            print('>>  3. 1st number must be less than 2nd number.')
            done2 = False
            done3 = False
            done3check = False
            print()
        else :
            done3check = True
    y = y + 1
    print('                              TABLE')
    print('Times ---------------------------------------------------------')
    if y - x <= 11 :
        for row in range(1,11,1) :
            if row < 10 :
                print('   ',end='')
            if row >= 10 and row <= 99 :
                print('  ',end='')
            print(row,'|',end='')
            for column in range(x,y,1) :
                product = row * column
                if product >= 100 and product <= 999 :
                    print('  ',end='')
                if product < 100 :
                    print('   ',end='')
                if product < 10 :
                    print(' ',end='')
                print(product,end='')
            print()
    condition = 'notvalid'
    while condition != 'valid' :
        print()
        userinput = input('* Press C to Continue or E to Exit : ')
        if userinput == 'c' or userinput == 'C' :
            print()
            done = c
            condition = 'valid'
        else :
            if userinput == 'e' or userinput == 'E' :
                done = e
                condition = 'valid'
            else :
                print()
                print('               >>>>>>>>>>>    Wrong Input !    <<<<<<<<<<<')
                condition = 'notvalid'
