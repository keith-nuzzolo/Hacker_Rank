'''
You are given a square map of size n×n.
Each cell of the map has a value denoting its depth.
We will call a cell of the map a cavity if and only if
this cell is not on the border of the map and each cell
adjacent to it has strictly smaller depth.
Two cells are adjacent if they have a common side (edge).

You need to find all the cavities on the map
 and depict them with the uppercase character X.
'''
def build_map(size):
    ''' takes size of map and then takes inputs based on the size needed and
    returns a map'''
    built_map = []
    for y in range(0, int(size)):
        built_map += [x for x in input().split()]
    return built_map

def test_cavity(map_, row, column):
    ''' takes the inputed map and coordinate and determines whether it is a
    cavity'''
    for row_ in range(row - 1, row + 2):
        if row_ == row:
            for column_ in range(column - 1, column + 2):
                if row_ == row and column_ == column:
                    pass
                elif map_[row_][column_] >= map_[row][column]:
                    return False
        else:
            if map_[row_][column] >= map_[row][column]:
                return False
    return True

def identify_cavity(mapped):
    '''takes the inputed map and determines where cavities are and returns
    a new map with cavities removed and replaced with an X '''
    new_map = []
    for line in mapped:
        new_map.append(line)
    for row in range(1,len(mapped) - 1):
        for column in range(1, len(mapped) - 1):
            if test_cavity(mapped,row,column):
                new_map[row] = new_map[row][:column] + 'X' + new_map[row][column +1:]
    return new_map

def cavity():
    ''' builds a map of inputed numbers, determines where caivities are and then
    prints the resulatant map'''
    initial_map = build_map(input())
    final_map = identify_cavity(initial_map)
    [print(final_map[x]) for x in range(0,len(final_map))]
cavity()
