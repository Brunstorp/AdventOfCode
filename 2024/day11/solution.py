stones = open('input.txt','r').readline().strip().split()
#stones = ['125','17']

def count_stones(stone, blinks, memo):
    
    if blinks == 0:
        return 1

    if (stone, blinks) in memo:
        return memo[(stone, blinks)]

    digits = len(stone)
    value = int(stone)

    if value == 0:
        result = count_stones('1', blinks - 1, memo)
        
    elif digits % 2 == 0:
        left = stone[:digits // 2].lstrip('0') or '0'
        right = stone[digits // 2:].lstrip('0') or '0'
        result = count_stones(left, blinks - 1, memo) + count_stones(right, blinks - 1, memo)
    else:
        new_stone = str(value * 2024)
        result = count_stones(new_stone, blinks - 1, memo)

    memo[(stone, blinks)] = result
    return result

memo = {}
part1 = sum(count_stones(stone, 25, memo) for stone in stones)
print(part1)
memo = {}
part2 = sum(count_stones(stone, 75, memo) for stone in stones)
print(part2)


        
        
        
        
    