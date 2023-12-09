def main():
    with open('input/input9', 'r') as f:
        lines = [list(map(int, l.split())) for l in f.readlines()]

    s = 0

    def next_ele(line):
        if (len(set(line)) == 1) and (0 in line):
            return 0
        deep_list = []
        for i in range(len(line)-1):
            deep_list.append(line[i+1]-line[i])
        return line[-1] + next_ele(deep_list)
  
    def prev(line):
        if (len(set(line)) == 1) and (0 in line):
            return 0
        deep_list = []
        for i in range(len(line)-1):
            deep_list.append(line[i+1]-line[i])
        return line[0] - prev(deep_list)
  
    for line in lines:
        s += next_ele(line)

    print(s)

    u = 0
    for line in lines:
        u += prev(line)

    print(u)
    

if __name__ == '__main__':
    main()
