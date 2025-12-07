def solve(text):
    grid = [list(s) for s in text.splitlines()]
    timelines = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    pt1_sol, pt2_sol = 0, 0
    for i in range(len(grid)-1):
        for j in range(len(grid[i])):
            c = grid[i][j]
            t = timelines[i][j]
            below = grid[i+1][j]
            if c == 'S':
                grid[i+1][j] = '|'
                timelines[i+1][j] = 1
            if c == '|':
                if below == '^':
                    if j > 0:
                        grid[i+1][j-1] = '|'
                        timelines[i+1][j-1] += t
                    if j < len(grid)-1:
                        grid[i+1][j+1] = '|'
                        timelines[i+1][j+1] += t
                    pt1_sol += 1
                else:
                    grid[i+1][j] = '|'
                    timelines[i+1][j] += t
    
    pt2_sol = sum(timelines[-1])
            
    return f'Part 1 solution: {pt1_sol}\nPart 2 solution: {pt2_sol}'
    
if __name__ == '__main__':
    with open('../input/day07') as f:
        print(solve(f.read()))