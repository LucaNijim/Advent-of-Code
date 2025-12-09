def check_fold(grid, i):
    print(f'Checking fold {i}...')
    errors = 0
    for c in range(min(i, len(grid)-i)):
        print(f'c = {c}')
        print(f'Checking row {i-(c+1)} against row {i+c}')
        if i == 2: 
            print(f'Row {i-(c+1)}: {grid[i-(c+1)]}')
            print(f'Row {i+c}: {grid[i+c]}')
        
        for j, low_row in enumerate(grid[i-(c+1)]):
            if grid[i+c][j] != low_row:
                errors += 1
    return errors


def folds(grid, smudge = 0):
    fs = []
    for i in range(1, len(grid)):
        # fold at {i} means u fold the rows < i against the rows => i.
        # example:
        # example: fold at 2 means u check 1 against 2 and 0 against 3.
        if check_fold(grid, i) == smudge:
            print(f'Grid can be folded along {i} with {smudge} smudges')
            fs.append(i)
        print(i)
    return fs

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

    # we want the ith row to become the ith column 

def solve(text):
    pt1sol, pt2sol = 0, 0
    grids = [[list(l) for l in t.splitlines()] for t in text.split('\n\n')]
    for grid in grids:
        
        print(grid)
        print(transpose(grid))
        # for transpose, we want ith row to become the ith column. 
        hf = [folds(grid, i) for i in range(2)]
        vf = [folds(transpose(grid), i) for i in range(2)]
        pt1sol += sum(vf[0]) + 100*sum(hf[0])
        pt2sol += sum(vf[1]) + 100*sum(hf[1])
        

    return f'Part 1 solution: {pt1sol}\nPart 2 solution: {pt2sol}'


if __name__ == '__main__':
    with open('input/input13') as f:
        print(solve(f.read()))