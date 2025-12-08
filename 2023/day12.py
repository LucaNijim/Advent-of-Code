from dataclasses import dataclass
from functools import lru_cache


@dataclass
class ConditionRecord:
    row: str = ""
    groups: tuple[int] = (0)
    curr_group: int = 0
    
    def __hash__(self):
        return hash((self.row, self.groups, self.curr_group))
    
    def __eq__(self, other):
        return self.row == other.row and self.groups == other.groups and self.curr_group == other.curr_group
    
    @lru_cache
    def num_arrangements(self):
        # first, do end conditions
        
        if len(self.row) == 0:
            ng = len(self.groups)
            if ng == 0 and self.curr_group == 0:
                return 1
            if ng == 1:
                if self.groups[0] == self.curr_group:
                    return 1
            return 0
            
        item = self.row[0]
        nc = ConditionRecord()
        match item:
            case ".":
                nc.row = self.row[1:]
                nc.curr_group = 0
                if self.curr_group > 0:
                    if self.curr_group == self.groups[0]:
                        nc.groups = self.groups[1:]
                    else:
                        return 0
                else:
                    nc.groups = self.groups
            case "#":
                if len(self.groups) == 0:
                    return 0
                if self.curr_group > self.groups[0]:
                    return 0
                else: 
                    nc.row = self.row[1:]
                    nc.groups = self.groups
                    nc.curr_group = self.curr_group + 1
            case "?":
                rv = 0
                for c in ('.', '#'):
                    rv += ConditionRecord(
                        c+self.row[1:],
                        self.groups, 
                        self.curr_group
                    ).num_arrangements()
                return rv
            case _:
                raise ValueError(f"Unknown condition type: {item}")
                       
        return nc.num_arrangements()

def solve(text):
    pt1_sol, pt2_sol = 0, 0
    for l in text.splitlines():
        rstr, gstr = l.split(" ")
        g = tuple(map(int, gstr.split(',')))
        cr = ConditionRecord(rstr, g)
        pt1_sol += cr.num_arrangements()
        g_pt2 = (*g, *g, *g, *g, *g)
        rstr_pt2 = (rstr+'?')*4+rstr
        pt2_sol += ConditionRecord(rstr_pt2, g_pt2).num_arrangements()
    return f'Part 1 solution: {pt1_sol}\nPart 2 solution: {pt2_sol}'

if __name__ == '__main__':
    condition_records = []
    with open('input/input12') as f:
        print(solve(f.read()))