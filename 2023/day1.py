def main():
    # First, we will do part 1
    day1_input = []
    with open('input/input1', 'r') as file:
        day1_input = file.readlines()
    
    part1_solution = 0
    part2_solution = 0

    str2num = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    
    def sumline(line):
        s = 0
        for char in line:
            if char.isdigit():
                s += 10*int(char)
                break
        for char in line[::-1]:
            if char.isdigit():
                s += int(char)
                break
        return s

    for line in day1_input:
        part1_solution += sumline(line)
        for key, val in str2num.items():
            line = line.replace(key, val)
        part2_solution += sumline(line)

    print(f'Part 1 solution: {part1_solution}')
    print(f'Part 2 solution: {part2_solution}')
 
if __name__ == '__main__':
    main()

