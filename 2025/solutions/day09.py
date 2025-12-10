from itertools import combinations as combs
        
    
class Line:
    def __init__(self, p1, p2):
        self.x1 = min(p1[0], p2[0])
        self.x2 = max(p1[0], p2[0])
        self.y1 = min(p1[1], p2[1])
        self.y2 = max(p1[1], p2[1])
        self.p1 = p1
        self.p2 = p2
        if self.x1 == self.x2:
            self.orientation = 'vert'
        elif self.y1 == self.y2:
            self.orientation = 'horz'
        else:
            raise ValueError('This function only accepts horizontal or vertical lines')
    
    def __repr__(self):
        return f"Line from ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})"
    
    def crosses(self, other):
        if self.orientation == 'vert':
            if other.orientation == 'horz':
                if other.x1 < self.x1 < other.x2 and self.y1 < other.y1 < self.y2:
                    return True
                
        if self.orientation == 'horz':
            if other.orientation == 'vert':
                if other.y1 < self.y1 < other.y2 and self.x1 < other.x1 < self.x2:
                    return True
        return False


class Rect:
    def __init__(self, p1, p2):
        self.x1 = min(p1[0], p2[0])
        self.x2 = max(p1[0], p2[0])
        self.y1 = min(p1[1], p2[1])
        self.y2 = max(p1[1], p2[1])

        self.top = Line((self.x1, self.y2), (self.x2, self.y2))
        self.bottom = Line((self.x1, self.y1), (self.x2, self.y1))
        self.left = Line((self.x1, self.y1), (self.x1, self.y2))
        self.right = Line((self.x2, self.y1), (self.x2, self.y2))
        self.sides = [self.top, self.bottom, self.left, self.right]

    def __repr__(self):
        return f"Rectangle from ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})"

    def area(self):
        return (self.x2 + 1 - self.x1) * (self.y2 + 1 - self.y1)

    def perturbed_by(self, line: Line):
        return (any(
            [line.crosses(side) for side in self.sides]
        )) or (self.contains(line.p1) or self.contains(line.p2)) or any((
            line.x1 == self.x1 and line.x2 == self.x2 and self.y1 < line.y1 < self.y2, 
            line.y1 == self.y1 and line.y2 == self.y2 and self.x1 < line.x1 < self.x2, 
        ))
    
    def contains(self, point):
        if self.x1 < point[0] < self.x2 and self.y1 < point[1] < self.y2:
            return True
        return False
            
def solve(text):
    pt1_sol, pt2_sol = 0, 0
    points = [tuple(map(int, l.split(','))) for l in text.splitlines()]
    lines = [Line(p, points[i-1]) for i, p in enumerate(points)]
    
    for i, (p1, p2) in enumerate(combs(points, 2)):
        
        print(f'Analyzing line {i} of {(len(lines)-1)*(len(lines))}')
        rect = Rect(p1, p2)
        pt1_sol = max(pt1_sol, rect.area())
        if not any([rect.perturbed_by(line) for line in lines]): pt2_sol = max(pt2_sol, rect.area())

    return f'Part 1 solution: {pt1_sol}\nPart 2 solution: {pt2_sol}'




if __name__ == '__main__':
    with open('../input/day09') as f:
        # plot(f.read())
        print(solve(f.read()))