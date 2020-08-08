from Cell import *


class BackTracking:
    """Back tracking algorithm to solve the sudoku"""

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.box_size = 3
        self.height = len(self.puzzle)
        self.width = len(self.puzzle[0])
        self.solved_puzzle = []
        self.number_of_element = self.width * self.height - 1  # -1 because we begin at 0
        self.current_index_of_puzzle = 0
        self.need_to_backward = False

    def get_row(self, row_number):
        return self.puzzle[row_number]

    def get_column(self, column_number):
        return [row[column_number] for row in self.puzzle]

    def get_box(self, row_number, column_number):
        """Return an array of the internal_box size already defined"""
        internal_box = [[0 for col in range(self.box_size)] for row in range(self.box_size)]
        row_start_box = (row_number // self.box_size) * self.box_size
        column_start_box = (column_number // self.box_size) * self.box_size
        for i in range(0, self.box_size):
            internal_box[i] = self.puzzle[row_start_box + i][column_start_box:column_start_box + self.box_size]
        return internal_box

    def initialize_game(self):
        """Initialize the cells in a new list"""
        for row in range(0, self.height):
            for col in range(0, self.width):
                self.solved_puzzle.append(Cell(row, col, self.get_box(row, col), self.puzzle, self.get_value(row, col)))

    def set_cell(self):
        """Find a new value for the current cell if not valid got backward in the list"""
        current_cell = self.solved_puzzle[self.current_index_of_puzzle]
        current_cell.puzzle = self.puzzle
        current_cell.internal_box = self.get_box(current_cell.row_number, current_cell.column_number)
        new_cell_value = current_cell.set_cell_value(self.need_to_backward)
        if new_cell_value != 0:
            self.need_to_backward = False
        else:
            self.need_to_backward = True
        self.puzzle[current_cell.row_number][current_cell.column_number] = current_cell.value
        current_cell.puzzle = self.puzzle
        current_cell.internal_box = self.get_box(current_cell.row_number, current_cell.column_number)

    def change_cell(self):
        """Go forward or backward in the list of cells"""
        if self.need_to_backward:
            self.current_index_of_puzzle -= 1
        else:
            self.current_index_of_puzzle += 1

    def solve(self):
        self.set_cell()
        self.change_cell()

    def run_solve(self):
        """Run the algorithm until the end of the grid is reached"""
        while self.current_index_of_puzzle < self.number_of_element:
            self.solve()

    def get_value(self, row_number, column_number):
        """Return the value of a cell according to its row and column"""
        return self.puzzle[row_number][column_number]
