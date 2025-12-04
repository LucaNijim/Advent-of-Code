from collections import defaultdict


def num_neighbors(k: int, grid: defaultdict):
    nbs = 0
    dirs = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
    for d in dirs:
        nbs += 1 if grid[d+k] == '@' else 0
    return nbs

def loc_few_nbs(grid: dict):
    grid_boundary = defaultdict(lambda: '.', grid)
    nbs = []
    for k, v in grid.items():
        if v == '@':
            if num_neighbors(k, grid_boundary) < 4:
                nbs.append(k)
    return nbs

def solve(text):
    grid = {}
    for r, line in enumerate(text.splitlines()):
        for c, ch in enumerate(line):
            grid[r+c*1j] = ch
    pt1sol = len(loc_few_nbs(grid))

    grids = [grid]
    incs = [float('inf')]
    while incs[-1] > 0:
        curr_grid = grids[-1]
        removes = loc_few_nbs(curr_grid)
        new_grid = curr_grid.copy()
        for k in removes: new_grid[k] = '.'
        grids.append(new_grid)
        incs.append(len(removes))
    pt2sol = sum(incs[1:])

    return f"Part 1 solution: {pt1sol}\nPart 2 solution: {pt2sol}"


if __name__ == "__main__":
    with open("../input/day04") as f:
        text = f.read()
        print(solve(text))