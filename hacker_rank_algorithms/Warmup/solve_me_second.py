'''
 It includes scanning two space-separated integers
 from STDIN in a loop over T lines, calling a function,
 returning a value, and printing that value to STDOUT.

SAMPLE INPUTS:
2
2 3
3 7
'''
cases = int(input())
for i in range(0, cases):
    num1 , num2 = input().split()
    num1, num2 = int(num1), int(num2)
    print(sum([num1, num2]))
