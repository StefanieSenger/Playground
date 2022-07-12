# checks whether a soduku solution is valid
'''I know it's not the most elegant or generalisable solution,
but this was what I could do pressed for time'''


def sudoku_validator(grid):
    rows = []
    rowsvalid = True
    columns = []
    columnsvalid = True
    squares = []
    squares1 = []
    squares2 = []
    squares3 = []
    squares4 = []
    squares5 = []
    squares6 = []
    squares7 = []
    squares8 = []
    squares9 = []
    squaresvalid = True
    for i in range(9):
        rows.append([grid[i][j] for j in range(9)])
    for j in range(9):
        columns.append([grid[i][j] for i in range(9)])
    for i in range(3):
        for j in range(3):
            squares1.append(grid[i][j])
            squares2.append(grid[i][j+3])
            squares3.append(grid[i][j+6])
            squares4.append(grid[i+3][j])
            squares5.append(grid[i+3][j+3])
            squares6.append(grid[i+3][j+6])
            squares7.append(grid[i+6][j])
            squares8.append(grid[i+6][j+3])
            squares9.append(grid[i+6][j+6])
            squares = [squares1, squares2, squares3, squares4, squares5, squares6, squares7, squares8, squares9]
    for ele in rows:
        if len(set(ele)) != 9:
            rowsvalid = False
    for ele in columns:
        if len(set(ele)) != 9:
            columnsvalid = False
    for ele in squares:
        if len(set(ele)) != 9:
            squaresvalid = False
    return rowsvalid & columnsvalid & squaresvalid


print(sudoku_validator(grid = [
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,7,2,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],

    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],

    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
]
))
