import re

def main():
    file = []
    with open('input/input2', 'r') as inputfile:
        file = inputfile.readlines()

    part1_limit = {'red':12, 'green':13, 'blue': 14}

    part1_solution = 5050
    part2_solution = 0

    for line in file:
        x = line.split(':')
        x[0] = int(x[0].lstrip('Game').strip(' \n'))
        y = re.split(';', x[1])
        possible = True
        temp_dict_pt2 = {'red':0, 'green':0, 'blue':0} 
        for i in y:
            for y in re.split(',', i):
                temp_dict_pt1 = {'red':0, 'green':0, 'blue':0} 
                num, key = y.strip().split()
                num = int(num)
                temp_dict_pt1[key] += num
                temp_dict_pt2[key] = max(temp_dict_pt2[key], num)
                for key in part1_limit.keys():
                    if temp_dict_pt1[key] > part1_limit[key]:
                        possible = False
        print(temp_dict_pt2)
        part2_solution += (temp_dict_pt2['red']*temp_dict_pt2['green']*temp_dict_pt2['blue'])
        if not possible:
            part1_solution -= x[0] 
 
    print(f'Part 1 solution: {part1_solution}')
    print(f'Part 2 solution: {part2_solution}')

    

if __name__ == '__main__':
    main()
