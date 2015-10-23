'''
You are given an integer N. Print the factorial of this number.

SAMPLE INPUT:
25
'''

def factorial(num):
    ''' takes factorial of inputed number and returns it
    '''
    total = 1
    for i in range(0,num):
        total = total * (num - i)
    return total
print(factorial(int(input())))
