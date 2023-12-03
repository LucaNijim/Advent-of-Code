def main():
    gameboard = []
    with open('input/input3', 'r') as file:
        for line in file.readlines():
            gameboard.append('.'+line.strip()+'.')
        gameboard.insert(0, '.'*len(gameboard[0]))
        gameboard.append('.'*len(gameboard[0]))
    
    part1_solution = 0
    for i in range(len(gameboard)):
        j = 0
        while j < len(gameboard[i]):
            if gameboard[i][j].isdigit():
                curr_dig = 0
                k = j+1
                while gameboard[i][j:k].isdigit():
                    curr_dig = int(gameboard[i][j:k])
                    k += 1
                is_diag_adjacent = False
                for l in (i-1, i, i+1):
                    for m in range(j-1, k):
                        if (gameboard[l][m] != '.') and (not gameboard[l][m].isdigit()):
                            is_diag_adjacent = True
                if is_diag_adjacent:    
                    part1_solution += curr_dig
                j = k 
            else:
                j += 1

    part2_solution = 0
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            if gameboard[i][j] == '*':
                numbers_around = []
                checked_points = set()
                for l in (i-1, i, i+1):
                    for m in (j-1, j, j+1):
                        if gameboard[l][m].isdigit() and ((l, m) not in checked_points):
                            checked_points.add((l, m))
                            n = m
                            o = m
                            while gameboard[l][n].isdigit():    
                                n -= 1
                                checked_points.add((l, n))
                            while gameboard[l][o].isdigit():
                                o += 1
                                checked_points.add((l, n))
                            numbers_around.append(int(gameboard[l][n+1:o])) 
                            
                if len(numbers_around) == 2:
                    part2_solution += numbers_around[0]*numbers_around[1]

    print(f'Part 1 solution: {part1_solution}')
    print(f'Part 2 solution: {part2_solution}')

if __name__ == '__main__':
    main()
