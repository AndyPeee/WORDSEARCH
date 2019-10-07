grid = [[]]
length=5
for i in range(length):
    grid.append([])
    graphnum = 1
    for increasingnum in range(length):
        grid[i].append(graphnum)
        graphnum = graphnum+1
for i in grid:
    print(i)
for numz in range(len(grid)):
    for j in range(len(grid[numz])):
        if grid[numz][j] == ' ':
            if grid[numz][numz] == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15:
                randholder = random.randint(0, 25)
                randletter = alphabet[randholder]
                grid[numz][numz] = randletter