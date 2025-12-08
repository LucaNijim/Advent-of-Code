from math import sqrt
from itertools import combinations as comb


def dist(p1, p2):
    return sqrt(sum([(p1[i]-p2[i])**2 for i in range(len(p1))]))

def solve(text):
    pt1_sol, pt2_sol = 0, 0
    
    points = [tuple(map(int, line.split(','))) for line in text.splitlines()]
    sorted_pairs = sorted(comb(points, 2), key=lambda p: dist(p[0], p[1]))
    circuits = set((p,) for p in points)
    
    for i, pair in enumerate(sorted_pairs):
        p1, p2 = sorted_pairs[i]
        sets = []
        for s in circuits:
            if p1 in s or p2 in s:
                sets.append(s)
        if len(sets) == 1:
            continue
        for s in sets: circuits.remove(s)
        circuits.add(sets[0]+sets[1])
        
        print(len(circuits))
        
        if len(circuits) == 1:
            pt2_sol = p1[0]*p2[0]
            break
        
        i += 1
        
        if i == 1000:
            pt1_sol = 1
            for circ in sorted(list(circuits), key=len)[-3:]:
                pt1_sol *= len(circ)
    
    return f"Part 1 solution: {pt1_sol}\nPart 2 solution: {pt2_sol}"

if __name__ == "__main__":
    with open("../input/day08") as f:
        print(solve(f.read()))