from math import floor
def ints_in_interval(a, b):
    return floor(b)-floor(a)

def solve(text):
    safe_dial = .50
    ep = 0.005
    pt1sol, pt2sol = 0, 0
    mapping = {'L': -1, 'R': 1}
    for inst in text.splitlines():
        sgn = mapping[inst[0]]
        inc = sgn*int(inst[1:])/100
        if inc < 0:
            pt2sol += ints_in_interval(inc+safe_dial- ep, safe_dial - ep)
        elif inc > 0:
            pt2sol += ints_in_interval(safe_dial + ep, safe_dial+inc + ep)
        safe_dial = round((safe_dial + inc) % 1, 2)
        safe_dial += (1 if safe_dial < 0 else 0)
        if -1*ep <= safe_dial <= ep:
            pt1sol += 1

    return f"Part 1 solution: {pt1sol}\nPart 2 solution: {pt2sol}"