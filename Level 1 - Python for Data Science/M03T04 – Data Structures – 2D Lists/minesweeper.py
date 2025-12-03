## A function to validate rows and columns inside the minegrid with boolean logic

    # This function tries to loop through each row in the minegrid using the command enumerate. It finds the row index and the row itself, which I called the line. It also checks if the column index is within the area for a row. This must be more than 0 but less than the length of the rows. True means the cell position exists and False shows it doesn't. The function was needed otherwise I kept getting errors in asking the program for rows that are not there. 

def mine_position(minegrid, row, col):
    for index, line in enumerate(minegrid):
        if index == row:
            if 0 <= col < len(line):
                return True
            else:
                return False
    return False


## Count adjacent mines around all cells inside the minegrid

    # Compass directions are turned into grid numbers like coordinates or cartesian points

def count_adj_mines(minegrid, row, col):
    compass_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for row_offset, col_offset in compass_directions:
        row_cell = row + row_offset
        col_cell = col + col_offset
        if mine_position(minegrid, row_cell, col_cell) and minegrid[row_cell][col_cell] == "#":
            count += 1
    return count


## Return the minegrid with numbers for each cell with no mine or hash for a mine

    # Nested for loop is used to gather the data needed

def minesweep_count(minegrid):
    result = []
    for row_index, row in enumerate(minegrid):
        row_result = []
        for col_index, cell in enumerate(row):
            if cell == "#":
                row_result.append("#")
            else:
                row_result.append(count_adj_mines(minegrid, row_index, col_index))
        result.append(row_result)
    return result


# Define a minefield of 5 x 7 size

minefield = [ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"], 
["#", "#", "-", "#", "-"],
["-", "#", "-", "-", "-"]]


# Print the results

minefield_scores = minesweep_count(minefield)
for score in minefield_scores:
    print(score)