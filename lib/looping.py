#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print (i)
        print ('Happy New Year!')
        i -= 1
    pass

def square_integers(int_list):
    squared_ints = [square ** 2 for square in int_list]
    print (squared_ints)
    squared_ints == None
    return squared_ints
pass

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')    
        else:
            print(i)  
    pass
