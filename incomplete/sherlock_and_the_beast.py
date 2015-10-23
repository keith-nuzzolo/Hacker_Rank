'''
his afternoon, Sherlock received a note from Moriarty, saying that he has infected 'The Beast' with a virus. Moreover,
the note had the number N printed on it.After doing some calculations,
Sherlock figured out that the key to remove the virus is the largest Decent Number having N digits.

A Decent Number has the following properties:

3, 5, or both as its digits. No other digit is allowed.
Number of times 3 appears is divisible by 5.
Number of times 5 appears is divisible by 3.

SAMPLE INPUT:
4
1
3
5
11
'''
def read_input():
    ''' reads input and returns the inpute as a int
    '''
    inputed = int(input())
    return inputed
def num_3(digits):
    ''' returns number of three's to put into the decent number
    '''
    num = 0
    if(digits % 5 == 0): 
        while digits > 0:
            digits +=  -5
            num += 1
    return num

def num_5(digits):
    ''' returns number of five's to put into the decent number
    '''
    num = 0
    if( digits % 3 == 0):
        while digits > 0:
            digits +=  -3
            num += 1
    else:
        while digits > 0 and digits % 3 != 0:
            digits += -3
            num += 1
    if digits % 5 == 0:
        return num
    else:
        return 0

def largest(num3, num5):
    ''' using number of three's and five's return largest decent number
    '''
    large = int('555' * num5 + '33333'* num3)
    return large
    
def decent_number(digits):
    ''' takes the number of digits and returns the largest decent number possible 
    '''
    decent_number = 0
    num5 = num_5(digits)
    digits = digits - (num5 * 3)
    num3 = num_3(digits)
    if num5 + num3 == 0:
        return -1
    else:
        return largest(num3, num5)

lines = int(input())
for i in range(0,lines):
    print (decent_number(read_input()))
        
