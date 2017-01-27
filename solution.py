


rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    "Cross product of elements in A and elements in B."
    return [s+t for s in a for t in b]


boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

diag1 = [rows[i] + cols[i] for i in range(len(rows))]
diag2 = [rows[i] + cols[-i-1] for i in range(len(rows))]
diag_units = [diag1, diag2]

#print row_units
#print column_units
#print square_units
#print diag_units

unitlist = row_units + column_units + square_units + diag_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def isThereNT(values, unit):
    '''Function identifies naked_twins within given unit
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
        unit(list): a list of boxes within unit ['A1', ...]
    Returns:
        NT(set): a set of Naked Twins {box_value, ...}
        
    '''
    # count values within unit
    count = {}
    for box in unit:
        # condition that satisfy naked twins definition 
        if len(values[box])==2:
            if values[box] in count:
                count[values[box]]+=1
            else:
                count[values[box]] = 1
    # naked twins set
    NT = {c for c in count if count[c] == 2}
    return NT


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    
    # creating a newValues dict to to store intermediate results
    newValues = dict()
    for unit in unitlist:
        # Find all instances of naked twins
        setNT = isThereNT(values, unit)
        # looping over naked twins and removing digits form their peers
        while len(setNT) > 0:

            NT = str(setNT.pop())
            
            d0 = NT[0]
            d1 = NT[1]
            # Eliminate the naked twins as possibilities for their peers
            for box in unit:
                if ((d0 in values[box]) or (d1 in values[box])) and (NT != values[box]):
                    newValues[box] = values[box].replace(d0,'')
                    newValues[box] = newValues[box].replace(d1,'')

    
    # propagating updated boxes to original instance of values    
    for v in newValues:
        values[v] = newValues[v]  
    
   
    return values


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
#    print len(grid)
#    print 'grid', grid
#    print grid[0]
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    sDict = {i:values[i] for i in values if len(values[i]) == 1}
        
    for i in sDict:
        for j in values:
            if i in peers[j]:
                values[j] = values[j].replace(sDict[i], '')
    return values

def only_choice(values):
    for unit in unitlist:
        for d in '123456789':
            ll = [box for box in unit if d in values[box]]
            if len(ll) == 1:
                values[ll[0]] = d
    
       
          
    return values

def reduce_puzzle(values):
    if type(values) == type('str'):
        values = grid_values(values)
        
        
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)

        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after

        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def solve(values):
#    values = grid_values(grid)
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
#    print values
    
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Chose one of the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Chose one of the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    
#    grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
#    grid1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    
#    diag_sudoku_grid = grid2
    
#    gv = grid_values(diag_sudoku_grid)
#    print gv
#    sol = solve(gv)
#    print sol


    display(solve(grid_values(diag_sudoku_grid)))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
