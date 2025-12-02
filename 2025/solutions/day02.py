# I just brute forced it today
def is_inv1(j):
    st = str(j)
    ln = len(st)
    return ln%2==0 and st[:ln//2] == st[ln//2:]


def is_inv2(j):
    st = str(j)
    ln = len(st)
    for i in range(1, ln//2+1):
        if ln % i == 0:
            if all([st[k:k+i] == st[0:i] for k in range(0, ln, i)]): return True
    return False


def solve(text):
    pt1sol, pt2sol = 0, 0
    for i in text.split(','):
        lb, ub = map(int, i.split('-'))
        for j in range(lb, ub+1):
            pt1sol += j if is_inv1(j) else 0
            pt2sol += j if is_inv2(j) else 0
    return f"Part 1 solution: {pt1sol}\nPart 2 solution: {pt2sol}"