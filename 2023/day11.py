def main():
    with open('input/input11_', 'r') as f:
        lines = f.readlines()

    null_rows, null_cols = set(), set()

    for i, row in enumerate(lines):
        if all([c=='.' for c in row]):
            null_rows.add(i)

    for j in range(len(lines[0])):
        if all([row[j] =='.' for row in lines)]):
            null_cols.add(j)

    

if __name__=='__main__':
    main()
