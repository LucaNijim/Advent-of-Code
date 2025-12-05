class ConditionRecord():
    def __init__(self, r, c):
        self.row = r
        self.criteria = c

    def __str__(self):
        return f'{self.criteria} {self.row}'

    def __repr__(self):
        return f'{self.criteria} {self.row}'

    def

def solve(text):
    return 'Sol'

if __name__ == '__main__':
    condition_records = []
    with open('input/input12') as f:
        for line in f:
            row, c = line.strip().split(' ')
            criteria = tuple(map(int, c.split(',')))
            condition_records.append(ConditionRecord(row, criteria))