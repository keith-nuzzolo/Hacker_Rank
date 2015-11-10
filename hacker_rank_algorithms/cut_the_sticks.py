'''
You are given N sticks, where the length of each stick is a positive integer.
 A cut operation is performed on the sticks such that all of them
 are reduced by the length of the smallest stick.

 Given the length of N sticks,
 print the number of sticks that are left before each subsequent cut operations.

 Sample Input #00

 6
 5 4 4 2 2 8
 '''

def cut(sticks):
    ''' takes a list of sticks in and applies a cut to them, then returns
    the list'''
    mini = min(sticks)
    zero = 0
    for i in range(0,len(sticks)):
        sticks[i] += -mini
        if sticks[i] == 0:
            zero += 1
    for a in range(zero):
        sticks.remove(0)
    return sticks

def parse_sticks(length, sticks):
    ''' takes the list of sticks and applies cuts until the list is empty'''
    sticks = [ int(x) for x in sticks.split()]
    while len(sticks) != 0:
        print (len(sticks))
        cut(sticks)


parse_sticks(input(), input())
