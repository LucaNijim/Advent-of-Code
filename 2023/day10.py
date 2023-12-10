import sys

def main():
    with open('input/input10', 'r') as f:
        lines = f.readlines()

    # Part 1 is a pretty straightforward breadth first search type of thing
    # Aside from silly mistakes, I didn't have too much of a tough time. 
    # I found the starting values to add to the queue manually,
    # I thought it would save time rather than having a conditional. 

    startpos = 0, 0

    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == 'S':
                startpos = x, y

    x, y = startpos
    
    queue = [(x+1, y, 1), (x-1, y, 1)]
    path = {(x, y):0}

    while queue:
        i, j, t = queue.pop(0)
        if (i, j) in path.keys():
            path[(i, j)] = min(path[(i, j)], t)
            continue
        path[(i, j)] = t
        match lines[i][j]:
            case '|':
                queue.append((i-1, j, t+1))
                queue.append((i+1, j, t+1))
            case '-':
                queue.append((i, j-1, t+1))
                queue.append((i, j+1, t+1))
            case 'L':
                queue.append((i, j+1, t+1))
                queue.append((i-1, j, t+1))
            case 'J':
                queue.append((i, j-1, t+1))
                queue.append((i-1, j, t+1))
            case '7':
                queue.append((i, j-1, t+1))
                queue.append((i+1, j, t+1))
            case 'F':
                queue.append((i+1, j, t+1))
                queue.append((i, j+1, t+1))

    print(f'Part 1 solution: {max(path.values())}')


    #Floodfill didn't work, and I feel like I somewhat understand why. 
    # We'll try a new strategy. Parity argument.  

    int_cells = 0
    for i, line in enumerate(lines):
        n_pipes = 0
        for j, c in enumerate(line):
            if (i, j) not in path and n_pipes%2==1:
                int_cells += 1
            elif (i, j) in path:
                match c:
                    case '|':
                        n_pipes += 1
                    case 'L':   
                        n_pipes += .5
                    case '7': 
                        n_pipes += .5
                    case 'J':
                        n_pipes -= .5
                    case 'F': 
                        n_pipes -= .5
                    case 'S':
                        n_pipes += 1

    print(f'Part 2 solution: {int_cells}')
                
        

if __name__ == '__main__':
    main()
