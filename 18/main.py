import copy

def tick(grid):
    def neighbor_count(x,y):
        total = 0
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                if dx == dy == 0: continue
                if 0 <= x+dx < width and 0 <= y+dy < height:
                    total += grid[y+dy][x+dx]
        return total

    height = len(grid)
    width = len(grid[0])
    result = copy.deepcopy(grid)
    for i in range(height):
        for j in range(width):
            if grid[j][i]:
                result[j][i] = neighbor_count(i,j) in (2,3)
            else:
                result[j][i] = neighbor_count(i,j) == 3
    return result

def light_corners(grid):
    for i in (0,99):
        for j in (0,99):
            grid[j][i] = True

for part in (1,2):
    with open("input") as file:
        grid = [[c == "#" for c in line.strip()] for line in file]

    if part == 2:
        light_corners(grid)

    for _ in range(100):
        grid = tick(grid)
        if part == 2:
            light_corners(grid)
    print(sum(sum(row) for row in grid))