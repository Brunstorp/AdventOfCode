import re
from functools import cmp_to_key #nice for lambdas
#I guess there's a more optimal solution but this works 
lines = [line.strip() for line in open('input.txt','r').readlines()]
first_section = lines[0:1177-1]
#print(first_section)
second_section = lines[1177:]
#print(second_section)

rules = {}

pattern = r'\b(\d{2})\|(\d{2})\b'
for line in first_section:
    match = re.findall(pattern, line)
    num1, num2 = match[0]
    rules[(num1,num2)] = -1
    rules[(num2,num1)] = 1
    
sum = 0
sum2 = 0
pattern = r'\d{2}'

for line in second_section:
    match = re.findall(pattern, line)
    N = len(match)
    #print(match)
    #print(match[N//2])
    
    if all( rules[(match[i], match[i+1])] == -1 for i in range(N-1) ):
        sum += int(match[N//2])
    else:
        match = sorted ( match, key=cmp_to_key(lambda left, right: rules[(left,right)]))
        sum2 += int(match[N//2])

print(sum) 
print(sum2)  
    
    
        
    

     
    
    

