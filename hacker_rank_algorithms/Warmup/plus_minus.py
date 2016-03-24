'''
You're given an array containing integer values.
You need to print the fraction of count of positive numbers,
negative numbers and zeroes to the total numbers.
Print the value of the fractions correct to 3 decimal places.

SAMPLE INPUT:
6
-4 3 -9 0 4 1 
'''

def count(inputs, size):
    ''' Take list of inputs and returns fraction of total for each type
    '''
    pos = 0
    neg = 0
    zero = 0
    for i in inputs:
        if(i > 0):
            pos += 1
        elif(i < 0):
            neg +=1
        else:
            zero +=1
    print(pos/size)
    print(neg/size)
    print(zero/size)

size = int(input())
inputs = [int(n) for n in input().split()]
count(inputs, size)
