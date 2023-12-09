def main():
    with open('input/input9', 'r') as f:
        lines = [list(map(int, l.split())) for l in f.readlines()]

    pt1, pt2 = 0, 0

    def next_ele(line):
        if all([not i for i in line]):
            return 0
        deep_list = []
        for i in range(len(line)-1):
            deep_list.append(line[i+1]-line[i])
        return line[-1] + next_ele(deep_list)
  
    for line in lines:
        pt1 += next_ele(line)
        pt2 += next_ele(line[::-1])

    print(f'Part 1 solution: {pt1}\nPart 2 solution: {pt2}')


if __name__ == '__main__':
    main()
