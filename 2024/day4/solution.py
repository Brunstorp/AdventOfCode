import re
from itertools import product

lines = [re.findall('.',line.strip()) for line in open('input.txt',"r").readlines()]

#i is the row, j is the column
def checker(i, j):
    search_word = "XMAS"
    directions = list(product((-1, 0, 1), (-1, 0, 1))) #Utilize cartesian product, I love math!
    directions.remove((0, 0))

    rows, cols = len(lines), len(lines[0])
    total_count = 0

    for di, dj in directions:
        word = []
        for step in range(4):  
            ni, nj = i + di * step, j + dj * step #This will ensure the directions are set up correctly 
            if 0 <= ni < rows and 0 <= nj < cols:  #assume as an example, di is negative, then we get the correct dirction
                word.append(lines[ni][nj])
            else:
                break
        if "".join(word) == search_word:
            total_count += 1

    return total_count

#part two checker
def checker2(i, j):
    search_words = {'MAS', 'SAM'}
    first = [(-1, -1), (0, 0), (1, 1)]
    second = [(-1, 1), (0, 0), (1, -1)]
    rows, cols = len(lines), len(lines[0])
    total_count = 0

    word1 = []
    for di, dj in first:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            word1.append(lines[ni][nj])
        else:
            break

    word2 = []
    for di, dj in second:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            word2.append(lines[ni][nj])
        else:
            break

    if "".join(word1) in search_words and "".join(word2) in search_words:
        total_count += 1

    return total_count


nbr_times_xmas = 0
nbr_times_mas = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'X':
            nbr_times_xmas += checker(i,j)
        if lines[i][j] == 'A':
            nbr_times_mas += checker2(i,j)


print(nbr_times_xmas)
print(nbr_times_mas)

