'''
You are given the height of the staircase. You need to print a staircase as shown in the example.

Example:
6
     #
    ##
    
   ###
  ####
 #####
######
'''

"""
def stairs(height):
    ''' prints staircase of inputed height
    '''
    [print(' '*(height-i)+'#'*i)for i in range(1,height+1)]
stairs(int(input()))
"""
def stairs(height):
    ''' prints staircase of inputed height
    '''
    [print('#'*i + ' '*(height-i))for i in range(1,height+1)]
stairs(int(input()))
