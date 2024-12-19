import numpy as np

directions = { 
    '^': np.array([-1, 0]),
    'v': np.array([1, 0]),
    '<': np.array([0, -1]),
    '>': np.array([0, 1])
}

def initialize_problem(filename="input.txt"):
    lines = [line.strip() for line in open(filename, 'r').readlines()]
    empty_row_index = lines.index('')
    game_map_lines = lines[:empty_row_index]
    instructions_lines = lines[empty_row_index + 1:]
    
    rows = len(game_map_lines)
    cols = len(game_map_lines[0])
    game_map = np.array([list(line) for line in game_map_lines], dtype='<U1')
    starting_point = np.argwhere(game_map == '@')[0]
    instructions = list("".join(instructions_lines))
    
    ##### PART TWO #####
    
    game_map_new = np.zeros((rows, 2*cols), dtype='<U1')
    
    for i in range(rows):
        for j in range(cols):
            if game_map[i, j] == '#':
                game_map_new[i, 2*j] = '#'
                game_map_new[i, 2*j+1] = '#'
            elif game_map[i, j] == 'O':
                game_map_new[i, 2*j] = '['
                game_map_new[i, 2*j+1] = ']'
            elif game_map[i, j] == '.':
                game_map_new[i, 2*j] = '.'
                game_map_new[i, 2*j+1] = '.'
            elif game_map[i, j] == '@':
                game_map_new[i, 2*j] = '@'
                game_map_new[i, 2*j+1] = '.'
                
    
    return game_map, instructions, starting_point, game_map_new

def solve(game_map, instructions, starting_point):
    current_position = np.array(starting_point)
    
    for instruction in instructions:
        direction = directions[instruction]
        new_position = current_position + direction
        
        if game_map[tuple(new_position)] == '#':
            continue
        
        if game_map[tuple(new_position)] == 'O':
            temp_position = new_position.copy()
            
            while game_map[tuple(temp_position)] == 'O':
                temp_position += direction
            
            if game_map[tuple(temp_position)] == '#':
                continue
            
            while not np.array_equal(temp_position, new_position - direction):
                game_map[tuple(temp_position)] = 'O'
                temp_position -= direction
            
            game_map[tuple(new_position)] = '@'
            game_map[tuple(current_position)] = '.'
            current_position = new_position
        else:
            game_map[tuple(new_position)] = '@'
            game_map[tuple(current_position)] = '.'
            current_position = new_position
            
    return game_map

def solve_part_two(game_map, instructions, starting_point):
    current_position = np.argwhere(game_map == '@')[0]
    
    pass

def get_gps(solved_map):
    positions = np.argwhere(solved_map == 'O')
    gps = 0
    for x,y in positions:
        gps += 100*x + y
    return gps

if __name__ == "__main__":
    game_map, instructions, starting_point, game_map_new = initialize_problem('test.txt')
    solved_map = solve(game_map, instructions, starting_point)
    print("\n".join("".join(row) for row in solved_map))
    print(get_gps(solved_map))
    
    ##### PART TWO #####
    
    print("\n".join("".join(row) for row in game_map_new))
    
    
