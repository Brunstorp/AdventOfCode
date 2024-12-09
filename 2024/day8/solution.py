import numpy as np
from itertools import combinations

def initiate_problem():
    map = np.array([ [x for x in line.strip()] for line in open("input.txt", 'r').readlines()])
    rows = len(map)
    cols = len(map[0])
    
    coordinates = {}
    for i in range(rows):
        for j in range(cols):
            pos = map[i][j]
            if pos != '.':
                coordinate = np.array([i,j])
                if pos in coordinates:
                    coordinates[pos].append(coordinate)
                else:
                    coordinates[pos] = [coordinate]
                    
    return coordinates, rows, cols

def get_node_points(a, b):
    AB = b - a #direction vector
    c = a - AB #point behind a
    d = b + AB #points behind b
    return c, d

def is_point_inside(rows, cols, point) -> bool: #returns true if that point is inside the map
    x,y = point
    return (0 <= x < rows) and (0 <= y < cols)

def get_antinodes(coordinates: dict, rows: int, cols: int):
    anti_nodes1 = set()
    anti_nodes2 = set()
    for frequency in coordinates:
        coordinate_list = coordinates[frequency]
        for a, b in combinations(coordinate_list, 2):
            #part 1
            for point in get_node_points(a,b):
                if is_point_inside(rows, cols, point):
                    anti_nodes1.add(tuple(point))
                    
            get_all_points(a,b, rows, cols, anti_nodes2) #this is for part 2
            
            
    part1 = len(anti_nodes1)
    part2 = len(anti_nodes2)
    
    return part1, part2
                
def get_all_points(a,b, rows, cols, anti_nodes):
    AB = b - a
    k = 0
    while True:
        c = a - k*AB
        k+=1
        if is_point_inside(rows, cols, c):
            anti_nodes.add(tuple(c))
        else:
            break
        
    k = 0     
    while True:
        d = b + k*AB
        k+=1
        if is_point_inside(rows, cols, d):
            anti_nodes.add(tuple(d))
        else:
            break
        
if __name__ == '__main__':
    coordinates, rows, cols = initiate_problem()
    amount1, amount2 = get_antinodes(coordinates, rows, cols)
    print(amount1)
    print(amount2)
    

    
    
    
    
    



    


