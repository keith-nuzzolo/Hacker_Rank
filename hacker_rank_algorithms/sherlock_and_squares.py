'''Watson gives two integers (A and B) to Sherlock
 and asks if he can count the number of square integers
  between A and B (both inclusive).

 Sample Input

2
3 9
17 24
'''
from math import *
def number_of_squares(a, b):
    ''' using the sarting and ending points a and b we return the number of
    perfect squares between them'''
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1

test_cases = int(input())
for x in range(0, test_cases):
    a = [int(x) for x in input().split()]
    print(number_of_squares(a[0],a[1]))
