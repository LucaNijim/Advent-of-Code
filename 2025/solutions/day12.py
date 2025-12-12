def solve(text):
    pt1, pt2 = 0, 0
    text = text.split("\n\n")
    blocks, lines = text[:-1], text[-1].split("\n")
    densities = [b.count('#') for b in blocks]
    no, maybe, yes = range(3)
    results = []
    for line in lines:
        xy, counts = line.split(': ')
        x, y = tuple(map(int, xy.split('x')))
        counts = tuple(map(int, counts.split(' ')))
        min_space = sum(a*b for a, b in zip(counts, densities))
        if x*y < min_space:
            results.append(no)
        elif (x//3)*(y//3) >= sum(counts):
            results.append(yes)
        else:
            results.append(maybe)
    print(f'Yes: {results.count(yes)}')
    print(f'No: {results.count(no)}')
    print(f'Maybe: {results.count(maybe)}')
    return pt1, pt2

if __name__ == '__main__':
    with open('../input/day12') as f:
        print(f'Solutions: {solve(f.read())}')