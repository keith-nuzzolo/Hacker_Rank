'''
You are given an array of integers of size N.
You need to print the sum of the elements in the array.

SAMPLE INPUT:
5
1000000001 1000000002 1000000003 1000000004 1000000005
'''
number = input()
arr = map(int, input().split())
print (sum(arr))
