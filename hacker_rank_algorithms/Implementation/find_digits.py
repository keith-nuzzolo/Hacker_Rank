'''
You are given an integer N
 Find the digits in this number that exactly divide N
 (division that leaves 0 as remainder)
 and display their count.
 Sample Input

2
12
1012
'''

def divide_exactly(number):
    ''' takes a number and determines how many of its units divide it
    exactly '''
    l = [int(x) for x in number[0:]]
    count = 0
    for i in l:
        if(i==0):
            pass
        elif int(number) % i == 0:
            count += 1
    return count

test_cases = int(input())
for i in range(test_cases):
    print( divide_exactly(input()))
