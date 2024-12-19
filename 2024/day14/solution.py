import re
import numpy as np

wide = 101
tall = 103

def initialize_problem():
    lines = [line.strip() for line in open('input.txt')]
    robots = []
    for line in lines:
        match = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
        if match:
            px, py, vx, vy = map(int, match.groups())
            print(px, py, vx, vy)
            robots.append({'position': (px, py), 'velocity': (vx, vy)})
    return robots


def count_robots_in_quadrants(robots):
    q1, q2, q3, q4 = 0, 0, 0, 0
    mid_x, mid_y = wide // 2, tall // 2

    for robot in robots:
        x, y = robot['position']
        if x == mid_x or y == mid_y:
            continue  # Skip robots on the boundary
        if x < mid_x and y < mid_y:
            q1 += 1
        elif x >= mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y >= mid_y:
            q3 += 1
        elif x >= mid_x and y >= mid_y:
            q4 += 1

    return q1, q2, q3, q4


def move_robot(robot):
    x, y = robot['position']
    vx, vy = robot['velocity']
    x = (x + vx) % wide
    y = (y + vy) % tall
    robot['position'] = (x, y)
      
if __name__ == '__main__':
    seconds = 100
    robots = initialize_problem()
    for i in range(seconds):
        for robot in robots:
            move_robot(robot)
            
    q1, q2, q3, q4 = count_robots_in_quadrants(robots)
    safety_factor = q1*q2*q3*q4
    print(safety_factor)
    

    
    
    