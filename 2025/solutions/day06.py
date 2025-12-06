from math import prod


def solve(text):
    lines = [line.split() for line in text.split('\n')]
    # part 1 
    nums, symbs = lines[:-1], lines[-1]
    pt1_sol = 0
    for i, symb in enumerate(symbs):
        if symb == '*':
            pt1_sol += prod([int(num[i]) for num in nums])
        elif symb == '+':
            pt1_sol += sum([int(num[i]) for num in nums])

    # part 2
    lines = text.split('\n')
    nums, symbs = lines[:-1], lines[-1]
    p1, p2 = len(symbs)-1, len(symbs)-1
    pt2_sol = 0
    while p2 > 0:
        while symbs[p1] == ' ':
            p1 -= 1
        # now we need to go from new p1 up to p2
        # column wise
        numbers = []
        for i in range(p1, p2+1):
            n = ''
            for l in nums:
                if l[i] != ' ':
                    n += l[i]
            numbers.append(n)
        if symbs[p1] == '+':
            pt2_sol += sum([int(n) for n in numbers])
        elif symbs[p1] == '*':
            pt2_sol += prod([int(n) for n in numbers])
        p1 -= 1
        p2 = p1-1


    return f'Part 1 solution: {pt1_sol}\nPart 2 solution: {pt2_sol}'

if __name__ == '__main__':
    with open('../input/day06') as f:
        print(solve(f.read()))
