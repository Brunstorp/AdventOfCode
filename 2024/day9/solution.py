
def initialize_problem():
    line = [[x for x in nbr] for nbr in open('input.txt', 'r')][0]
    #line = [[x for x in nbr] for nbr in open('test.txt', 'r')][0]
    #print(line)
    instructions = []
    
    ID = 0
    
    for i,nbr in enumerate(line):
        nbr = int(nbr)
        if nbr == 0:
            continue
        
        temp = None
        if not i % 2:
            temp = ID
            ID += 1
        else: 
            temp = '.'
         
        to_extend = [temp]*nbr
        instructions.extend(to_extend)
        
        
    
    
    return instructions

def increment_left(instructions, left):
    for i in range(left+1, len(instructions)):
        if instructions[i] == '.':
            left = i
            return left
        
    return left
    
def increment_right(instructions, right):
    for i in range(right-1,-1,-1):
        if instructions[i] != '.':
            right = i
            return right
    return right

def move_file(instructions):
    left = 0
    right = len(instructions)
    element = None
    while left < right:
        left = increment_left(instructions, left)
        right = increment_right(instructions, right)
        #print(left, right)
        #print(instructions)
        element = instructions[right]
        instructions[right] = '.'
        instructions[left] = element 
    
    instructions = instructions[0:right+1]
    instructions[-1] = element #added the last element? For some reason I always miss it
    return instructions    
    
def calc_check_sum(instructions):
    sum = 0
    for i, nbr in enumerate(instructions):
        if nbr == '.':
            continue
        sum += i*int(nbr)
    return sum

def move_blocks(instructions):
    n = len(instructions)
    last_symbol = None
    for i in range(n-1,-1,-1): #start is from the right, end is leftmost
        current_symbol = instructions[i]
        if current_symbol != '.' and current_symbol != last_symbol:
            block_high = i
            block_low = i
            starting_symbol = current_symbol
            next_symbol = current_symbol
            
            while next_symbol == starting_symbol:
                next_symbol = instructions[block_low-1]
                if next_symbol != starting_symbol:
                    break
                block_low -= 1
            block_length = block_high - block_low + 1 
            
            for j in range(block_low):
                if all(c == '.' for c in instructions[j:j + block_length]):
                    instructions[j:j + block_length] = instructions[block_low:block_high+1]
                    instructions[block_low:block_high+1] = ['.'] * block_length
    
        last_symbol = current_symbol
        
    return instructions






if __name__ == '__main__':
    instructions = initialize_problem()
    #print(instructions)
    #print(ranges)
    
    copy_instructions = instructions.copy() 
    
    new_instructions = move_file(instructions)
    check_sum = calc_check_sum(new_instructions)
    print(check_sum) #part 1
    
    new_instructions = move_blocks(copy_instructions)
    #print(new_instructions)
    
    check_sum = calc_check_sum(new_instructions)
    print(check_sum)
