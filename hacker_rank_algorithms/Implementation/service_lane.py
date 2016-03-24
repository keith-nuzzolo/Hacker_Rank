'''Calvin is driving his favorite vehicle on the 101 freeway
 He notices that the check engine light of his vehicle is on,
  and he wants to service it immediately to avoid any risks.
  Luckily, a service lane runs parallel to the highway.
  The length of the service lane is N units.
   The service lane consists of N segments of equal length and different width.

Calvin can enter to and exit from any segment.
Let's call the entry segment as index i and the exit segment as index j.
 Assume that the exit segment lies after the entry segment (i≤j) and 0≤i.
  Calvin has to pass through all segments from index i to index j
  (both inclusive).
  Sample Input

8 5
2 3 1 2 3 2 3 3
0 3
4 6
6 7
3 5
0 7
'''
def which_type(test, width):
    ''' takes the test and the width of the freeway and determines what the
    biggest vehicle is and returns it'''
    return min(width[test[0]: test[1]+1])

def parse_through(num_cases, width):
    ''' takes in the number of test cases and the width of the road and
    takes inputs to put into which_type to return the vehicle type'''
    for i in range(0, num_cases):
        test = [int(x) for x in input().split()]
        print(which_type(test, width))
length_and_test_cases = [int(x) for x in input().split()]
width = [int(x) for x in input().split()]
parse_through(length_and_test_cases[1], width)
