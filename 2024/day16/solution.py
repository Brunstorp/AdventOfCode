import numpy as np
import heapq
from collections import defaultdict

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def add_to_graph(graph, node, matrix):
    if node not in graph:
        graph[node] = set()
    
    for direction in directions.values():
        new_node = (node[0] + direction[0], node[1] + direction[1])
        
        if 0 <= new_node[0] < matrix.shape[0] and 0 <= new_node[1] < matrix.shape[1]:
            if matrix[new_node] != '#':
                graph[node].add(new_node)
                if new_node not in graph:
                    graph[new_node] = set()
                graph[new_node].add(node)

def initialize_problem(file_path="input.txt"):
    matrix = np.array([[x for x in line.strip()] for line in open(file_path, 'r').readlines()])
    graph = {}
    start, end = None, None

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == '#':
                continue
            node = (i, j)
            if matrix[i, j] == 'S':
                start = node
            if matrix[i, j] == 'E':
                end = node
            add_to_graph(graph, node, matrix)

    return graph, start, end

def calculate_turn_cost(previous_direction, movement_direction):
    dot_product = np.dot(previous_direction,movement_direction)
    if dot_product > 0:
        return 1 
    else:
        return 1001  

def dijkstras(graph, start, end):
    
    initial_direction = (0, 1)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, initial_direction))
    prev = {}
    minimum_costs = {}
    minimum_costs[(start, initial_direction)] = 0

    while priority_queue:
        current_cost, current_node, previous_direction = heapq.heappop(priority_queue)

        if current_node == end:
            continue

        for neighbor in graph[current_node]:
            movement_direction = (neighbor[0] - current_node[0], neighbor[1] - current_node[1])
            turn_cost = calculate_turn_cost(previous_direction, movement_direction)
            tentative_cost = current_cost + turn_cost

            if tentative_cost < minimum_costs.get((neighbor, movement_direction), float('inf')):
                minimum_costs[(neighbor, movement_direction)] = tentative_cost
                prev[(neighbor,previous_direction)] = (current_node,movement_direction)
                heapq.heappush(priority_queue, (tentative_cost, neighbor, movement_direction))

    best_cost = min(minimum_costs[(end, d)] for d in directions.values() if (end, d) in minimum_costs)
    best_states = [(end, d) for d in directions.values() if (end, d) in minimum_costs and minimum_costs[(end, d)] == best_cost]

    return best_cost, None

if __name__ == "__main__":
    graph, start, end = initialize_problem('test.txt')
    result_cost, best_nodes = dijkstras(graph, start, end)
    print("Shortest path cost from 'test.txt':", result_cost)
    print("Number of tiles on at least one best path (test.txt):", best_nodes)

    graph, start, end = initialize_problem('test2.txt')
    result_cost, best_nodes = dijkstras(graph, start, end)
    print("Shortest path cost from 'test2.txt':", result_cost)
    print("Number of tiles on at least one best path (test2.txt):", best_nodes)

    graph, start, end = initialize_problem('input.txt')
    result_cost, best_nodes = dijkstras(graph, start, end)
    print("Shortest path cost from 'input.txt':", result_cost)
    print("Number of tiles on at least one best path (input.txt):", best_nodes)
