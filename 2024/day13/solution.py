import re

cost_A = 3
cost_B = 1
to_add = 10000000000000

def solve(x_a, y_a, x_b, y_b, p_x, p_y):
    B = round(p_y - p_x*y_a/x_a) / (y_b - y_a*x_b/x_a)
    A = round(p_x-B*x_b) / x_a

    return 3*A + B if (
        int(A*x_a + B*x_b) == p_x
        and int(A*y_a + B*y_b) == p_y
    ) else None
    
def initialize_problem(filename='test.txt'):
    lines = [line.strip() for line in open(filename, 'r').readlines() if len(line.strip()) > 0]
    return lines

def solve_problem(lines):
    total_cost = 0
    for i in range(0, len(lines), 3):
        button_a = re.search(r'Button A: X\+(\d+), Y\+(\d+)', lines[i])
        button_b = re.search(r'Button B: X\+(\d+), Y\+(\d+)', lines[i+1])
        prize = re.search(r'Prize: X=(\d+), Y=(\d+)',lines[i+2])
        
        button_a_x, button_a_y = map(int, button_a.groups())
        button_b_x, button_b_y = map(int, button_b.groups())
        
        prize_x, prize_y = map(int, prize.groups())
        prize_x += to_add
        prize_y += to_add
        solution = solve(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y)
        
        if solution is not None:
            cost = solution
            total_cost += cost

    print(f"Total Cost: {total_cost}")

if __name__ == '__main__':
    lines = initialize_problem('input.txt')
    solve_problem(lines)