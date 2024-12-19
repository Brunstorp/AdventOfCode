import numpy as np

garden = None
def flood_fill(garden, type, visited, coordinate, region_coords): #apparently used in image processing
    x,y = coordinate
    if x < 0 or y < 0 or x >= garden.shape[0] or y >= garden.shape[1]:
        return
    if visited[x][y] == 1:
        return
    if garden[x][y] != type:
        return
    visited[x][y] = 1
    region_coords.append((x,y))
    flood_fill(garden, type, visited, (x+1,y),region_coords)
    flood_fill(garden, type, visited, (x-1,y),region_coords)
    flood_fill(garden, type, visited, (x,y+1),region_coords)
    flood_fill(garden, type, visited, (x,y-1),region_coords)

def find_regions(garden):
    visited = np.zeros(garden.shape)
    regions = {}
    
    for i in range(garden.shape[0]):
        for j in range(garden.shape[1]):
            if visited[i,j] == 0:
                region_coords = []
                flood_fill(garden, garden[i,j], visited, (i, j), region_coords)
                if garden[i,j] not in regions:
                    regions[garden[i,j]] = []
                regions[garden[i,j]].append(region_coords)
    
    return regions
                    
def calc_perim(region, garden, type):
    perimeter = 0
    for coord in region:
        x,y = coord
        if x == 0 or garden[x-1][y] != type:
            perimeter += 1
        if x == garden.shape[0]-1 or garden[x+1][y] != type:
            perimeter += 1
        if y == 0 or garden[x][y-1] != type:    
            perimeter += 1      
        if y == garden.shape[1]-1 or garden[x][y+1] != type:
            perimeter += 1
    return perimeter

def calc_area(region):
    return len(region)

def initialize_problem(filename = 'input.txt'):
    garden = np.array([[x for x in line.strip()] for line in open(filename  ,'r').readlines()])
    return garden

if __name__ == '__main__':
    garden = initialize_problem('test.txt')
    regions = find_regions(garden)
    total_price = 0
    for type, region in regions.items():
        for r in region:
            area = calc_area(r)
            perimeter = calc_perim(r, garden, type)
            total_price += area*perimeter    
    print(total_price)
                 
    
    
            

