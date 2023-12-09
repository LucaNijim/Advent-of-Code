import re
import math

def main(): 
    with open('input/input8') as f:
        l = [line.strip() for line in f.readlines()]
        inst = list(map(int, l[0].translate(str.maketrans('LR', '01'))))
    maps = {}
    for line in l[2:]:
        n = re.split('([A-Z]+) = \\(([A-Z]+), ([A-Z]+)\\)', line)
        maps[n[1]] = n[2], n[3] 

    i = 0 
    m = len(inst)
    pos = 'AAA'
    while pos != 'ZZZ':
        pos = maps[pos][inst[i%m]]
        i = i+1

    its = []

    for p in maps.keys():
       
        if p[2] == 'A':
            pos = p
            i = 0
            while pos[2] != 'Z':
                pos = maps[pos][inst[i%m]]
                i += 1
            its.append(i)

    print(f'Part 1 solution: {i}')
    print(f'Part 2 solution: {math.lcm(*its)}')

if __name__=='__main__':
    main()
