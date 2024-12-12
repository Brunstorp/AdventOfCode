import numpy as np
from collections import deque
def add_edge(coord,matrix,rows,cols):
    
    x,y = coord
    value = matrix[coord]
    possible_nodes = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    nodes_to_add= []
    for node in possible_nodes:
        nodex, nodey = node
        if 0<= nodex < rows and 0<= nodey < cols:    
            if matrix[node] == value + 1:
                nodes_to_add.append(node)
    return nodes_to_add
    


def initalize_problem():
    matrix = np.array([[int(x) for x in line.strip()] for line in open("input.txt",'r').readlines()])
    #matrix = np.array([[int(x) for x in line.strip()] for line in open("test.txt",'r').readlines()])
    graph = {}
    starting_positions = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            coord = (i,j)
            edges_to_add = add_edge(coord, matrix,rows,cols)
            graph[coord] = edges_to_add
            if matrix[coord] == 0:
                starting_positions.append(coord)
    return graph, starting_positions, matrix

def BFS(graph, start_node,matrix):
    visited = set()
    queue = deque([start_node])
    result = []

    while queue:
        current_node = queue.popleft()
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if matrix[current_node] == 9:
            result.append(current_node)
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return result

def recursive_DFS(graph, current_node, current_path, all_paths, visited, matrix):
    current_path.append(current_node)

    if matrix[current_node] == 9:
        all_paths.append(current_path[:])

    for neighbor in graph[current_node]:
        if neighbor not in visited:
            visited.add(neighbor)
            recursive_DFS(graph, neighbor, current_path, all_paths, visited, matrix)
            visited.remove(neighbor)

    current_path.pop()
    
def solve_problem_part1(graph,starting_positions,matrix):
    sum = 0
    #print(starting_positions)
    #print(graph)
    for start_node in starting_positions:
        nines = BFS(graph,start_node,matrix)
        sum += len(nines)
        
    print(sum)
    
def solve_problem_part2(graph,starting_positions,matrix):
    sum = 0
    
    for start_node in starting_positions:
        all_paths = []
        visited = set([start_node])
        recursive_DFS(graph,start_node,[],all_paths,visited,matrix)
        sum += len(all_paths)
    print(sum)
               
if __name__ == '__main__':
    graph, starting_positions, matrix = initalize_problem()
    solve_problem_part1(graph,starting_positions,matrix)
    solve_problem_part2(graph,starting_positions,matrix)
    
     
                
                
        
            

            