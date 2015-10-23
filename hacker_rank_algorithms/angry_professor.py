'''
Given the arrival time of each student, your task is to find out if the class gets cancelled or not.

SAMPLE INPUTS:
2
4 3
-1 -3 4 2
4 2
0 -1 2 1
'''
def is_canceled(s_min,arrive):
    ''' Takes the mininum number and the arrival times and returns whether class is canceled
    '''
    on_time = []
    for i in arrive:
        if( i <= 0 ):
            on_time.append(i)
    if(len(on_time) >= int(s_min)):
        return 'NO'
    else:
        return 'YES'
def use_inputs(size):
    ''' uses the inputed size to return the program the correct number of times
    '''
    for i in range(0, size):
        students = input()
        s = students.index(' ')
        L = [int(x) for x in input().split()]
        print(is_canceled(students[s:], L))

size = int(input())
use_inputs(size)


