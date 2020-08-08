class Cell:
    def __init__(self, row_number, column_number, internal_box, puzzle, value):
        self.row_number = row_number
        self.column_number = column_number
        self.puzzle = puzzle
        self.internal_box = internal_box
        self.value = value
        self.possibilities = set(range(1, 10))
        self.solved = True if self.value > 0 else False  # if the number already exists at the beginning

    def check_number_validity(self, number):
        """Check if the number is already in the row or column or box"""
        for unit_array in [self.internal_box]:
            if any(number in sublist for sublist in unit_array):  # if the value is already there

                return False
        for unit_array1 in [self.puzzle[self.row_number], [row[self.column_number] for row in self.puzzle]]:
            if number in unit_array1:  # if the value is already there
                return False
        return True

    def set_cell_value(self, backward):
        """Return the new value of the cell if it is valid or return 0"""
        if not self.solved:  # if the number was not in the grid at the beginning
            to_delete_in_set = []
            for elt in self.possibilities:  # check in all possibilities
                if self.check_number_validity(elt):
                    self.value = elt
                    for elem in to_delete_in_set:
                        self.possibilities.remove(elem)
                    return elt
                else:
                    to_delete_in_set.append(elt)
            self.reset_set()
            self.value = 0
            return 0
        else:
            if backward:  # if already in backward continue and pass the fixed number
                return 0
            else:
                return self.value

    def reset_set(self):
        self.possibilities = set(range(1, 10))
