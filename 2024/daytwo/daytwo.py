lines = open("inputtwo.txt", "r").readlines()
reports = [ [int(x) for x in line.strip().split()] for line in lines]
nbr_safe = 0
fixable = []
for report in reports:
    if all( earlier < later and 1<= abs(earlier-later) <= 3 for earlier, later in zip(report, report[1:])) or all( earlier > later and 1<= abs(earlier-later) <= 3 for earlier, later in zip(report, report[1:])):
        nbr_safe += 1
    else:
        fixable.append(report)
        
print(nbr_safe)
## Part two

for report in fixable:
    first_remove = False
    for j in range(len(report)):
        test = report[:j] + report[j+1:]
        if all( earlier < later and 1<= abs(earlier-later) <= 3 for earlier, later in zip(test, test[1:])) or all( earlier > later and 1<= abs(earlier-later) <= 3 for earlier, later in zip(test, test[1:])):
            if not first_remove:
                first_remove = True
            else: #then we must have popped it before and therefore already used dampener
                break
            nbr_safe += 1
    

print(nbr_safe)
                
                
            
            
       
            
        
        
    



    
        
    
        
        
        
        
        
    
    

    
