from collections import Counter

def val(l, pt):
    # This function creates a bijection from cards to natural numbers that maintains ordering. 
    # it lets us use the built in python sorting algorithm with the function as the key. 
    # if C is the list of counts of cards, it returns the sum of counts squared times a large number
    # so it dominates the rest. 
    # After that, it just maps the special characters to hex digits
    # and converts them to an integer, simply using place value to do the rest of the orderings. 
    h = l.split()[0].translate(str.maketrans('TJQKA', 'abcde' if pt==1 else 'a1cde'))
    if h == '11111': # Special case
        return int('11111', 16)+25*10e8
    match pt:
        case 1:
            c = sum(i**2 for i in Counter(h).values())
        case 2:
            co = Counter(h)
            j = co['1']
            del co['1'] 
            c = sorted(list(co.values()))
            c[-1]+=j
            c = sum(i**2 for i in c)

    return int(h, 16)+c*10e8

def main():
    with open('input/input7', 'r') as f:
        lines = f.readlines()
    for part in (1, 2):
        sol = sum([(i+1)*int(line.split()[1]) for i, line in enumerate(sorted(lines, key=lambda x: val(x, part)))])
        print(f'Part {part} solution: {sol}')

if __name__ == '__main__':
    main()
