'''
The Utopian Tree goes through 2 cycles of growth every year.
The first growth cycle occurs during the spring, when it doubles in height.
 The second growth cycle occurs during the summer,
 when its height increases by 1 meter.

Now, a new Utopian Tree sapling is planted at the onset of spring. Its height is 1 meter.
 Can you find the height of the tree after N growth cycles?

 Sample Input:

3
0
1
4
'''
def growth(cycle_numbers):
    ''' Takes current height of tree and its number of growth cycles and returns the new
    height of the tree'''
    current_height = 1
    for i in range(1, cycle_numbers + 1):
        if(i % 2 == 0):
            current_height += 1
        else:
            current_height += current_height
    return current_height

def cycle(number_of_cycles):
    ''' takes number of cycles and calls upon the growth function to determine
    and return the height of the tree after the growth cycles'''
    for i in range(0, number_of_cycles):
        print(growth(int(input())))
cycle(int(input()))
