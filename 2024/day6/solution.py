import numpy as np

'''
    UP (-1,0)
    DOWN  (1,0)
    LEFT  (0,-1)
    RIGHT  (0,1)
'''

def find_start(rows,cols,matrix):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "^":
                start_pos = (i, j)
                return start_pos
    

def rotate_vector_right(direction):
    x, y = direction
    return (y, -x)

def add_vectors(A, B):
    x1, y1 = A
    x2, y2 = B
    return (x1 + x2, y1 + y2)

def check_next(next_x, next_y, matrix):
    if not (0 <= next_x < rows and 0 <= next_y < cols):
        return "DONE"
    if matrix[next_x][next_y] == "#":
        return "OBSTACLE"
    return "MOVE"

def get_next(curr_direction, curr_position,matrix):
    next_position = add_vectors(curr_position, curr_direction)
    next_x, next_y = next_position
    while check_next(next_x, next_y,matrix) == "OBSTACLE":
        curr_direction = rotate_vector_right(curr_direction)
        next_position = add_vectors(curr_position, curr_direction)
        next_x, next_y = next_position
    return next_position, curr_direction

def walk(start_pos, matrix): # "Up" direction is (0, -1) returns true if cycle found
    path_walked = set()
    start_direc=(-1,0)
    cycle_path=set()
    curr_position = start_pos
    curr_direction = start_direc
    
    while True:
        path_walked.add(curr_position)
        cycle_path.add((curr_position,curr_direction))
        next_position, curr_direction = get_next(curr_direction, curr_position,matrix)
        next_x, next_y = next_position
        
        if (next_position, curr_direction) in cycle_path:
            return True, path_walked
            
        if check_next(next_x, next_y, matrix) == "DONE":
            return False, path_walked
        
        curr_position = next_position

def find_cycles(path_walked, matrix):
    
    nbr_cycles = 0
    new_path = path_walked
    new_path.remove(start_pos)
    
    for obs_x,obs_y in new_path:
         #I Add both the position and direction as ((posx,posy),(dirx,diry))
        new_matrix = np.copy(matrix)
        new_matrix[obs_x][obs_y] = "#"
        check_cycle, path = walk(start_pos,new_matrix)
        if check_cycle:
            nbr_cycles += 1
            
    print(nbr_cycles)

matrix = np.array([list(line.strip()) for line in open("input.txt", "r").readlines()])
rows = len(matrix)
cols = len(matrix[0])
start_pos = find_start(rows,cols,matrix)

_, path_walked = walk(start_pos, matrix)

sum_X = len(path_walked)
print(sum_X)   

#PART TWO
find_cycles(path_walked,matrix)



