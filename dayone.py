#take in the lists, sort them, take distance between all, sum them up

lines = open("inputone.txt", "r").readlines()
N = len(lines)
sortedleft = [0 for i in range(N)]
sortedright = [0 for i in range(N)]
sum = 0
for i,line in enumerate(lines):
    x = line.strip().split()
    sortedleft[i] = int(x[0])
    sortedright[i] = int(x[1])
    
sortedleft = sorted(sortedleft)
sortedright = sorted(sortedright)

for i in range(N):
    sum += abs(sortedleft[i] - sortedright[i])
    
print(sum)

## part two
simscore = 0

for i in range(N):
    left = sortedleft[i]
    simscore += left * sortedright.count(left)
print(simscore)




    
    


    
    
    
    
