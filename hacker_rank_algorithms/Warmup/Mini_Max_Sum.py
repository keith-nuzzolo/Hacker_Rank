'''
Given five positive integers, find the minimum and maximum values
that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line
of two space-separated long integers.
'''
import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
sorted_list = sorted([a,b,c,d,e])
print(sum(sorted_list[0:4]), sum(sorted_list[1:5]))
