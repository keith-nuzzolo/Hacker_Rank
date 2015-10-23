'''
You are given co-ordinates of N "random" triangles,
find the number of triangles for which the interior contains the origin.

SAMPLE INPUT:
2
-1 -2 1 -2 1 3
-2 -1 -2 1 -1 2
'''

def cross(x, y , x1 , y1):
    ''' takes the cross product of two inputed vectors and returns value
    '''
    return x * y1 - y *x1




num = int(input())
triangles = []
g = []
for i in range(0, num):
    g = [int(n) for n in input().split()]
    triangles.append(g)
print(triangles)
