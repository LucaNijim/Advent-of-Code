def main():
    # Below is my part 1 solution, it should be pretty understandable. 
    with open('input/input6', 'r') as file:
        text = file.readlines()
        times = map(int, text[0].split(':')[1].strip().split())
        distances = list(map(int, text[1].split(':')[1].strip().split()))
    
    part1sol = 1

    for i, time in enumerate(times):
        ways = 0
        for t in range(time+1):
            if t*(time-t) > distances[i]:
                ways += 1

        part1sol *= ways
        # This just tries each value in the range

    print(f'Part 1 solution: {part1sol}')

    # We observe that doing the brute force approach would be too slow. 
    # Instead, we do a binary search on the function described below to find its zeros.

    part2_time = int(text[0].split(':')[1].replace(' ', ''))
    part2_dist = int(text[1].split(':')[1].replace(' ', ''))

    # zeros of func
    # f(t) = t(time-t)-distances
    
    def f(t):
        return t*(part2_time-t)-part2_dist

    # find solutions using this binary search

    t = 0
    def find_0(t, p):
        shift = 10
        error = 100000 # start with smaller for practice input. 
        while abs(error) > 0.1:
            new_error = f(t)
            if new_error < 0:
                t += shift*p
                if error > 0:
                    shift /= 2
            elif new_error > 0:
                t -= shift*p
                if error < 0:
                    shift /= 2
            error = new_error
        return t

    print(f'Part 2 solution: {int(find_0(part2_time, -1))-int(find_0(0, 1))}')

    # In hindsight, I am a dumbass and could have used the quadratic formula. 

if __name__ == '__main__':
    main()
