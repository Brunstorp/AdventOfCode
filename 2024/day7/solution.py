from itertools import product

lines = [line.strip().split() for line in open("input.txt","r").readlines()]

#we need to build something that builds all combinations, if that doesnt work let's do recursively (i.e too big), I can use #eval(string) command
#*,+

def get_combinations(N, part1=True): #this creates all the combinations of * and +, and then I realised I can't use || so | instead
    if part1:
        operators = ['*', '+']
        combinations = [''.join(p) for p in product(operators, repeat=N)]
        return combinations
    
    operators = ['*', '+', '|']
    combinations = [''.join(p) for p in product(operators, repeat=N)]
    #print(combinations)
    return combinations


def evaluate_left_to_right(expression, part1 = True):
    if part1:
        while len(expression) > 1:
            expression = [ str( eval(''.join(expression[:3]) ) ) ] + expression[3:]
        return int(expression[0])
    
    result = int(expression[0])
    
    for i in range(1, len(expression), 2):
        operator = expression[i]  
        next_number = int(expression[i + 1]) 
        
        if operator == '+':
            result += next_number
        elif operator == '*':
            result *= next_number
        elif operator == '|':
            result = int(str(result) + str(next_number)) 
            
    return result
    
def build_expression(numbers, combination):
    expression = [a for pair in zip(numbers, combination) for a in pair]
    expression.append(numbers[-1])
    return expression

def part1(lines):
    sum = 0
    for line in lines:
        
        number = int(line[0][:-1])
        numbers = line[1:]
        N = len(numbers)-1 #right... N must be 1 less otherwise crash (they are in between)
        combinations = get_combinations(N)
        
        for combination in combinations:
            expression = build_expression(numbers, combination)
            #print(expression)
            if evaluate_left_to_right(expression) == number:
                sum += number
                break
            
    return sum

def part2(lines):
    sum = 0
    for line in lines:
        number = int(line[0][:-1])
        numbers = line[1:]
        N = len(numbers)-1 #right... N must be 1 less otherwise crash (they are in between)
        combinations = get_combinations(N, part1=False)
        
        for combination in combinations:
            expression = build_expression(numbers, combination)
            #print(expression)
            if evaluate_left_to_right(expression, part1=False) == number:
                sum += number
                break
            
    return sum
            
#part one         
sum = part1(lines)  
print(sum) 

## Part two   
sum2 = part2(lines)
print(sum2)


    
