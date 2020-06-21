# Sudoku Solver
# Shay Brennan-Kelly

class Sudoku_Puzzle: 
    def __init__(self, starting_grid):
        self.box = self.setup_puzzle_grid() 
        self.row = self.initialise_rows()
        self.column = self.initialise_columns()
        self.grid = self.initialise_and_flatten_grid(starting_grid)
        self.predefined_numbers = self.find_indices_of_predfined_numbers()

    # Initialises indices for each cell in entire grid
    def setup_puzzle_grid(self):
        box = []
        box.append([0, 1, 2, 9, 10, 11, 18, 19, 20])
        box.append([3, 4, 5, 12, 13, 14, 21, 22, 23])
        box.append([6, 7, 8, 15, 16, 17, 24, 25, 26])
        box.append([27, 28, 29, 36, 37, 38, 45, 46, 47])
        box.append([30, 31, 32, 39, 40, 41, 48, 49, 50])
        box.append([33, 34, 35, 42, 43, 44, 51, 52, 53])
        box.append([54, 55, 56, 63, 64, 65, 72, 73, 74])
        box.append([57, 58, 59, 66, 67, 68, 75, 76, 77])
        box.append([60, 61, 62, 69, 70, 71, 78, 79, 80])
        return box
    
    # Initialises indices for cells in each row
    def initialise_rows(self):
        row = []
        for i in range(0, 81, 9):
            row.append(range(i, i+9))
        return row
    
    # Initialises indices for cells in each column
    def initialise_columns(self):
        column = []
        for i in range(9):
            column.append(range(i, 80+i, 9))
        return column
    
    # Takes the 2D grid representing the puzzle, 
    # replaces all the '.' with zeros and converts it to a 1D list
    def initialise_and_flatten_grid(self,starting_grid):
        for i in range(0,9):
            starting_grid[i] = [x if isinstance(x,int) else 0 for x in starting_grid[i]]
        return [item for row in starting_grid for item in row]

    # Creates list of numbers pre-filled on the supplied puzzle 
    # We need to track as these values should not be updated by the solver
    def find_indices_of_predfined_numbers(self):
        predefined_numbers = []*len(self.grid)
        for i in self.grid:
            if i > 0:
                predefined_numbers.append(True)
            else:
                predefined_numbers.append(False)
        return predefined_numbers

    # Validates if a value can be entered in a cell
    # Checks against current row, column and box 
    # for potential collisions
    def is_valid_value(self, number, index):
        # Ran into an issue with the indices not easily converting from 
        # float to int here with Python 3, runs fine with Python 2.7 though
        current_row = index/9
        current_column = index%9
        current_box = (current_row/3)*3 + (current_column/3)
        for i in self.row[current_row]:
            if (self.grid[i] == number):
                return False
        for i in self.column[current_column]:
            if (self.grid[i] == number):
                return False
        for i in self.box[current_box]:
            if (self.grid[i] == number):
                return False
        return True

    # Utility Function to convert contents of the grid to a string
    def to_string(self): 
        grid_string = ""
        for i in range(9):
            grid_string += (self.grid[i*9:i*9+9]) 

    # Utility Function to print contents of the grid 
    def print_grid(self): 
        for i in range(9):
            print (self.grid[i*9:i*9+9]) 

    # Checks if there are any zeros left in grid, 
    # may allow us exit loop earlier than just iterating 1 to 81
    def contains_zeros(self):
        return self.grid.count(0) > 0

    def solve_puzzle(self):
        i = 0
        proceed = True
        # While we still have 0/empty cells and in range
        while(self.contains_zeros() and i < 81):
            # If this was pre-filled, we either go forward or back 1 step
            if self.predefined_numbers[i]:
                if proceed:
                    i += 1
                else:
                    i -= 1
            else:
                # Otherwise, we test values 1 through 9
                number = self.grid[i]
                prev = self.grid[i]
                while(number < 9):
                    if (number < 9):
                        number += 1
                    # If we find a value that works, stop searching and 
                    # move on to another cell
                    if self.is_valid_value(number, i):
                        self.grid[i] = number
                        proceed = True
                        break
                # If value found matches the previous value, 
                # assign to false and try another cell
                if (self.grid[i] == prev):
                    self.grid[i] = 0
                    proceed = False
                if proceed:
                    i += 1
                else:
                    i -=1

# Main method, validating method against data/example in problem sheet
if __name__ == '__main__': 
    starting_grid=[
        [5,3,'.','.',7,'.','.','.','.'],
        [6,'.','.',1,9,5,'.','.','.'],
        ['.',9,8,'.','.','.','.',6,'.'],
        [8,'.','.','.',6,'.','.','.',3],
        [4,'.','.',8,'.',3,'.','.',1],
        [7,'.','.','.',2,'.','.','.',6],
        ['.',6,'.','.','.','.',2,8,'.'],
        ['.','.','.',4,1,9,'.','.',5],
        ['.','.','.','.',8,'.','.',7,9]
    ]

    puzzle = Sudoku_Puzzle(starting_grid)

    print("Input :")
    puzzle.print_grid()

    puzzle.solve_puzzle()

    print("Solution: ")
    puzzle.print_grid()
