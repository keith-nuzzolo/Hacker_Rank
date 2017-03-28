'''
Sam's house has an apple tree and an orange tree that yield an abundance of fruit.
In the diagram below, the red region denotes his house, where s is the start
point and t is the end point. The apple tree is to the left of his house,
and the orange tree is to its right.
You can assume the trees are located on a single point, where the apple tree is
at point a and the orange tree is at point b.
When a fruit falls from its tree, it lands d units of distance from its tree of
origin along the x-axis. A negative value of d means the fruit fell d units
to the tree's left, and a positive value of d means it falls d units to the
tree's right.

Given the value of d for m apples and n oranges,
can you determine how many apples and oranges will fall on Sam's house
(i.e., in the inclusive range[s,t])?
Print the number of apples that fall on Sam's house as your first line of output,
then print the number of oranges that fall on Sam's house as your
second line of output.
'''
import sys

import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
on_house =0;
for i in apple:
    if(((a+i)>=s and (a+i)<=t)):
        on_house += 1
print(on_house)
on_house =0
for i in orange:
    if(((b+i)>=s and (b+i)<=t)):
        on_house += 1
print(on_house)
