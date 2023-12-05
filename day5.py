def main():
    with open('input/input5', 'r') as file:
        inputs, *blocks = file.read().split('\n\n')
    seeds = [int(x) for x in inputs.split(':')[1].split()]
    seedranges_1 = [(x, x+1) for x in seeds]
    seedranges_2 = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
    print(f'Part 1 solution: {minmap(seedranges_1, blocks)}')
    print(f'Part 2 solution: {minmap(seedranges_2, blocks)}')

def minmap(seedranges, blocks):
    for block in blocks:
        newranges = [] # we will add the new ranges to this
        maps = [tuple(map(int, line.split())) for line in block.splitlines()[1:]]

        while len(seedranges) > 0:
            cs, ce = seedranges.pop()
            # current start, current end
            for a, b, c in maps:
                # check if there is overlap
                os, oe = max(b, cs), min(ce, b+c)
                if os < oe:
                    newranges.append((os-b+a, oe-b+a))
                    if cs < os:
                        seedranges.append((cs, os))
                    if oe < ce:
                        seedranges.append((oe, ce))
                    break
            else:
                newranges.append((cs, ce))

        seedranges = newranges

    return min(map(min, seedranges))

# We will create a mapping class for each of the maps: seed-soil, soil-fertilizer, etc. 

if __name__ == '__main__':
    main()
