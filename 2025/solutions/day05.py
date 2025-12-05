def range_union(range1: tuple[int], comp_range: tuple[int]):
    if comp_range[0] <= range1[0] and comp_range[1] >= range1[1]:
        return comp_range[0], comp_range[1]
    elif comp_range[0] <= range1[0] and comp_range[1] >= range1[0]:
        return comp_range[0], range1[1]
    elif comp_range[0] <= range1[1] and comp_range[1] >= range1[1]:
        return range1[0], comp_range[1]
    elif comp_range[0] >= range1[0] and comp_range[1] <= range1[1]:
        return range1[0], range1[1]
    else:
        return None

def solve(text):
    ranges, ingredients = [x.split("\n") for x in text.split("\n\n")]
    ranges = [ tuple(map(int, r.split('-'))) for r in ranges]
    ingredients = map(int, ingredients)
    pt1sol = 0

    # first, do part 2, mutate ranges

    disjoint_ranges = set()
    while len(ranges) > 0:
        curr_range = ranges.pop()
        disjoint = True
        for r in disjoint_ranges:
            if range_union(r, curr_range):
                disjoint = False
                disjoint_ranges.remove(r)
                ranges.append(range_union(r, curr_range))
                break
        if disjoint:
            disjoint_ranges.add(curr_range)

    pt2sol = sum([x[1]-x[0]+1 for x in disjoint_ranges])

    # now only use the disjoint ranges!

    for ing in ingredients:
        for r in disjoint_ranges:
            if r[0] <= ing <= r[1]:
                pt1sol += 1
                break

    return f"Part 1 solution: {pt1sol}\nPart 2 solution: {pt2sol}"


if __name__ == "__main__":
    with open("../input/day05") as f:
        text = f.read()
    print(solve(text))