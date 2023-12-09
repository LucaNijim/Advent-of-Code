from collections import defaultdict

def main(): 
    part1_solution = 0
    part2_solution = 0
    num_cards = {}
    with open('input/input4', 'r') as file:
        for i in range(len(file.readlines())):
            num_cards[i]=1
    with open('input/input4', 'r') as file:
        for num, card in enumerate(file.readlines()):
            card = card.split(':')[1].split('|') 
            winning_numbers = set(card[0].split()) 
            num_winningnums = 0
            for number in card[1].split():
                if number in winning_numbers:
                    num_winningnums += 1
            if num_winningnums > 0:
                for i in range(num+1, num+num_winningnums+1):
                    num_cards[i] += num_cards[num]
                part1_solution += 2**(num_winningnums-1)

    print(f'Part 1 solution: {part1_solution}')
    print(num_cards)
    for key, val in num_cards.items():
        part2_solution += val
    print(f'Part 2 solution: {part2_solution}')
    

if __name__ == '__main__':
    main()
