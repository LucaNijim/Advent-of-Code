from collections import deque

import numpy as np
from scipy.optimize import milp, LinearConstraint


class Machine():
    def __init__(self, input_string: str):
        indicator, *buttons, joltage_reqs = input_string.split(' ')
        self.indicator = tuple(int(c=='#') for c in indicator[1:-1])
        self.joltage_reqs = tuple(map(int, joltage_reqs[1:-1].split(',')))
        self.buttons = tuple(eval(c[:-1]+',)') for c in buttons)
        
        # print(self.indicator)
    
    def pt1(self):
        # what are we doing here? 
        # the idea: work through state space of possible button presses
        # they could be represented as sorted tuples. 
        # each number would be a button to press 
        # this means they could be added to a set
        queue = deque()
        for i, _ in enumerate(self.buttons): queue.append((i,))
        tried = set()
        
        # bfs on button space basically!
        # not fully optimized
        while True:
            # get indices from queue
            button_indices = queue.popleft()
            
            # see the actions of that button sequence
            ex_indicator = [0 for _ in self.indicator]
            for index in button_indices:
                # print(f'Pressing button {index}: {self.buttons[index]}')
                for i in self.buttons[index]:
                    ex_indicator[i] += 1
            
            # verify
            # print(f'buttons: {button_indices}')
            # print(f'ex_indicator: {ex_indicator}')
            if tuple(map(lambda x: x%2, ex_indicator)) == self.indicator:
                # print(f'Buttons {[self.buttons[i] for i in button_indices]} works!!!')
                return len(button_indices)
            
            # add to queue
            for i, _ in enumerate(self.buttons):
                new_indices = tuple(sorted(button_indices + (i,)))
                if new_indices in tried:
                    continue
                tried.add(new_indices)
                queue.append(new_indices)
    def pt2(self):
        b = np.array(self.joltage_reqs)
        n, p = len(self.joltage_reqs), len(self.buttons)
        A = np.zeros(shape=(n, p))
        for j, button in enumerate(self.buttons):
            # the buttons form the column space
            for i in button:
                A[i,j] = 1
        # now we just want to find x in N^p
        # such that Ax=b
        # minimizing |x|_1
        
        # one way is to first look for hard constraints? 
        # if row i has sum 1, then x[i]=b[i]
        # idk 
        res = milp(
            c = np.ones(shape=(p,)), 
            integrality = np.ones(shape=(p,)),
            constraints = LinearConstraint(A, lb = b, ub = b)
        )
        return int(sum(res.x)) 
        
        
            
        

def solve(text):
    pt1_sol, pt2_sol = 0, 0
    for line in text.splitlines():
        m = Machine(line)
        pt1_sol += m.pt1()
        pt2_sol += m.pt2()
        
        
    return f'Part 1 solution: {pt1_sol}\nPart 2 solution: {pt2_sol}'

if __name__ == "__main__":
    with open("../input/day10") as f:
        print(solve(f.read()))