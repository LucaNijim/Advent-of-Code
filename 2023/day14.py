def transpose(g: list[list]):
    # len(grid[0]) is number of columns in list 
    row_length = len(g[0])
    ng = [[] for _ in enumerate(g[0])]
    for row in g:
        if row_length != len(row):
            raise ValueError('Rows of grid have unequal length')

        for i, item in enumerate(row):
            ng[i].append(item)
    return ng


def slide_row(row):
    wall_index, ptr = 0, 0
    new_row = []
    while len(new_row) < len(row):
        if ptr >= len(row):
            while len(new_row) < len(row):
                new_row.append('.')
            break
        char = row[ptr]
        match char:
            case 'O':
                new_row.append(char)
                wall_index += 1
                ptr += 1
            case '.':
                ptr += 1
            case '#':
                while len(new_row) < ptr:
                    new_row.append('.')
                new_row.append(char)
                wall_index = ptr
                ptr += 1
    return new_row


def slide(g: list[list], direction = 'left'):
    if direction == 'left':
        new_grid = []
        for row in g:
            new_grid.append(slide_row(row))
        return new_grid
    elif direction == 'right':
        new_grid = []
        for row in g:
            new_grid.append(slide_row(row[::-1])[::-1])
        return new_grid
    elif direction == 'up':
        return transpose(slide(transpose(g), 'left'))
    elif direction == 'down':
        return transpose(slide(transpose(g), 'right'))
    else:
        raise ValueError('Direction not understood')
    


def weight(pt1grid: list[list]):
    total = 0
    for i, row in enumerate(pt1grid[::-1]):
        for char in row:
            if char == 'O':
                total += (i+1)
    return total

def solve(text):
    pt1_sol, pt2_sol = 0, 0
    grid = [list(row) for row in text.splitlines()]
    
    pt1_sol = weight(slide(grid, 'up'))

    directions = ['up', 'left', 'down', 'right']
    grids = [grid]
    for cycle in range(1000000000):
        curr_grid = grids[-1]
        for direction in directions:
            curr_grid = slide(curr_grid, direction)
        grids.append(curr_grid)
        if grids[-1] in grids[:-1]:
            # we found a cycle
            i1 = grids.index(grids[-1], 0, -1)
            i2 = cycle + 1
            print(f'i1 = {i1}, i2 = {i2}')
            print(f'i1 weight = {weight(grids[i1])}, i2 weight = {weight(grids[i2])}')
            print(f'Weights from i1 to i2: {[weight(g) for g in grids[i1:i2+1]]}')
            pt2_sol = weight(grids[(1000000000-i1)%(i2-i1)])
            break
        # try:
        #     print(f'Weight of grid after cycle {cycle}: {weight(grids[-1])}')
        #     if grids[-1] == grids[-2]:
        #         pt2_sol = weight(grids[-1])
        #         break
        # except IndexError:
        #     continue
    
    # print(slide(grid, 'left'))
    return f'Part 1 solution: {pt1_sol}, Part 2 solution: {pt2_sol}'

if __name__ == '__main__':
    with open('input/input14') as f:
        print(solve(f.read()))
        print(slide_row(['O', '#', '.', 'O']))