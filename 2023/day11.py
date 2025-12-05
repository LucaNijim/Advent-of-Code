from itertools import combinations


def main():
    with open('input/input11', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    # lines = """...#.#
    # ...#..""".split('\n')
    pt1_sol, pt2_sol = 0, 0

    null_rows, null_cols = [], []

    for i, row in enumerate(lines):
        if all([c=='.' for c in row.strip()]):
            null_rows.append(i)

    for j, _ in enumerate(lines[0]):
        if all([row[j] =='.' for row in lines]):
            null_cols.append(j)
    # build galaxy dict
    galaxies = set()
    for i, r in enumerate(lines):
        for j, c in enumerate(r):
            if c == '#':
                galaxies.add((i, j))
    pairs = list(combinations(galaxies, 2))

    for pair in pairs:
        g1, g2 = pair
        md = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        # first ele is row #
        # second ele is col #
        for c in null_rows:
            if min(g1[0], g2[0]) <= c <= max(g1[0], g2[0]):
                pt1_sol += 1
                pt2_sol += 999999
        for c in null_cols:
            if min(g1[1], g2[1]) <= c <= max(g1[1], g2[1]):
                pt1_sol += 1
                pt2_sol += 999999
        pt1_sol += md
        pt2_sol += md
    print(f'Part 1: {pt1_sol}\nPart 2: {pt2_sol}')


if __name__=='__main__':
    main()
