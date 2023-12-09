import time 

def main():
    start = time.time()
    with open('input/input5', 'r') as file:
        lines = file.readlines()
    seeds = [int(x) for x in lines[0].split(':')[1].split()]
    lines = lines[2:]
    part1_solution = min(map(lambda x: seedmap(x, lines), seeds))
    print(f'Part 1 solution: {part1_solution}')
    seedranges = []
    for i, seed in enumerate(seeds):
        if i%2==0:
            seedranges.append([seed])
        else: 
            seedranges[-1].append(seed)
    minval = float('inf')
    for seedrange in seedranges:
        minval = min(map(lambda x: seedmap(x, lines), range(seedrange[0], sum(seedrange))))
    part2_solution = minval
    print(f'Part 2 solution: {part2_solution}')
    end = time.time()
    with open('day5output', 'w') as file:
        file.write(f'Part 1 solution: {part1_solution}\n')
        file.write(f'Part 2 solution: {part2_solution}\n')
        file.write(f'Time elapsed: {end-start}\n')
     

def seedmap(seed, lines):
    inst_lists = [[]]
    for i, line in enumerate(lines):
        if line[0].isalpha():
            continue
        elif line == '\n':
            inst_lists.append([])
        else:
            inst_lists[-1].append(line.strip('\n'))
    #print(inst_lists)
    for sublist in inst_lists:
        #print(f'current seed: {seed}')
        ind = True
        for nums in sublist:
            #print(nums)
            num1, num2, num3 = nums.split()
            if (int(num2) <= seed) and (seed < int(num2)+int(num3)):
                #print(f'mapping based on {nums}')
                seed = int(num1) + (seed-int(num2))
                break
        #print(f'maps to {seed}')
    return seed

if __name__ == '__main__':
    main()
