class Memoize():
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key in self.cache:
            return self.cache[key]
        value = self.func(*args, **kwargs)
        self.cache[key] = value
        return value
    
    
@Memoize
def n_paths(graph, st, end):
    if st == end:
        return 1
    try:
        return sum(n_paths(graph, n, end) for n in graph[st])
    except KeyError:
        return 0

def solve(text):
    g = {}
    for line in text.splitlines():
        a, b = line.split(':')
        g[a] = [c for c in b.split()]
    pt1_sol = n_paths(g, 'you', 'out')
    svr_fft = n_paths(g, 'svr', 'fft')
    pt2_sol = sum((
        n_paths(g, 'svr', 'fft') * n_paths(g, 'fft', 'dac') * n_paths(g, 'dac', 'out'),
        n_paths(g, 'svr', 'dac') * n_paths(g, 'dac', 'fft') * n_paths(g, 'fft', 'out')
    ))
    
    return f'Part 1 solution: {pt1_sol}\nPart 2 solution: {pt2_sol}'
                
    
    
if __name__ == '__main__':
    with open('../input/day11') as f:
        print(solve(f.read()))