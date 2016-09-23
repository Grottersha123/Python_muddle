def count_neighbours(grid, row, col):
    count = 0
    for x,y in ((row - 1, col), (row + 1, col), (row, col - 1),(row, col + 1), (row - 1, col - 1), (row - 1, col + 1),(row + 1, col - 1), (row + 1, col + 1)):
        print (grid[x])
        print (y)

        """if(0 <= x < len(grid) and 0 <= y < len(grid[x])): 
            if grid[x][y]:
                count += 1
    return count
    """
                    
count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2)