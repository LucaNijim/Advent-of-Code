def joltage(line: str, n: int):
    if n == 1:
        return max(map(int, line))
    i = 0
    d1 = 0
    for j in range(len(line)-n+1):
        if int(line[j]) > d1:
            d1 = int(line[j])
            i = j
    return 10**(n-1)*d1 + joltage(line[i+1:], n-1)

def solve(text):
    pt1sol, pt2sol = 0, 0
    for battery in text.splitlines():

        pt1sol += joltage(battery, 2)
        pt2sol += joltage(battery, 12)
    return f"Part 1 solution: {pt1sol}\nPart 2 solution: {pt2sol}"
