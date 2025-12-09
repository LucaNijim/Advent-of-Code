from itertools import combinations as combs
import matplotlib.pyplot as plt 


class Rect:
    def __init__(self, p1, p2):
        self.x1 = min(p1[0], p2[0])
        self.x2 = max(p1[0], p2[0])
        self.y1 = min(p1[1], p2[1])
        self.y2 = max(p1[1], p2[1])
    
    def __repr__(self):
        return f"Rectangle from ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})"

    def area(self):
        return (self.x2+1-self.x1) * (self.y2+1-self.y1)
    
class Face:
    def __init__(self, p1, p2, orientation=0):
        self.x1 = p1[0]
        self.x2 = p2[0]
        self.y1 = p1[1]
        self.y2 = p2[1]
        self.orientation: int = orientation
        
    def __repr__(self):
        return f'Face from ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})'

class VertFace(Face):
    def __init__(self, p1, p2, orientation=0):
        super().__init__(p1, p2, orientation)
        if self.x1 != self.x2:
            raise ValueError(f"x1 {self.x1} != x2 {self.x2}")
        self.x = self.x1
        

class HorzFace(Face):
    def __init__(self, p1, p2, orientation=0):
        super().__init__(p1, p2, orientation)
        if self.y1 != self.y2:
            raise ValueError(f"y1 {self.y1} != y2 {self.y2}")
        self.y = self.y1
        
    
class TilePolygon():
    def __init__(self, points):
        self.faces = []

        
        # rewrap points list to start from leftmost vertical face
        first_leftmost_vf_index = 0
        for i, p in enumerate(points):
            if p[0] < points[first_leftmost_vf_index][0]:
                first_leftmost_vf_index = i
        points = points[first_leftmost_vf_index:]+points[:first_leftmost_vf_index]
        self.faces.append(VertFace(points[0], points[1], 1))
                        
        for i, p in enumerate(points)[1:]:
            np = points[i+1]
            prev_face = self.faces[-1]
            if isinstance(prev_face, HorzFace):
        


def solve(text):
    pt1_sol, pt2_sol = 0, 0
    points = [tuple(map(int, l.split(','))) for l in text.splitlines()]
    for p1, p2 in combs(points, 2):
        pt1_sol = max(pt1_sol, Rect(p1, p2).area())
    tp = TilePolygon(points)
    return f'Part 1 solution: {pt1_sol}\nPart 2 solution: {pt2_sol}'

    
def plot(text):
    pairs = [tuple(map(int, l.split(','))) for l in text.splitlines()]
    fig, ax = plt.subplots()
    for i, p in enumerate(pairs):
        pp = pairs[i-1]
        ax.plot([p[0], pp[0]], [p[1], pp[1]])
    plt.show()
        
    
    

if __name__ == '__main__':
    with open('../input/day09') as f:
        #plot(f.read())
        print(solve(f.read()))