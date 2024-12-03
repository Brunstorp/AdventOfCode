import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
mult = 0
lines = [line for line in open("input.txt", "r").readlines()]

for line in lines:
    matches = re.findall(pattern, line.strip())
    for match in matches:
        num1, num2 = map(int, match)
        mult += num1 * num2

print(mult)

## Part two

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
pattern2 = r"\d{1,3}"
on = True
mult = 0

for line in lines:
    matches = re.findall(pattern, line.strip())
    for match in matches:
        print(match)
        if match == "do()":
            on = True
            continue
        elif match == "don't()":
            on = False
            continue
        if on:
            num1, num2 = map(int,re.findall(pattern2, match))
            mult += num1*num2
 
print(mult)
   
        
