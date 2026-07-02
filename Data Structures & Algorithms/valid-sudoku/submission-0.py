class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)] # Create a list of sets to track numbers in each row
        cols = [set() for _ in range(9)] # Create a list of sets to track numbers in each column
        boxes = [set() for _ in range(9)] # Create a list of sets to track numbers in each 3x3 box

        for i in range(9): # Iterate through each row
            for j in range(9): # Iterate through each column
                num = board[i][j] # Get the current number on the board
                if num != '.': # Ignore empty cells represented by '.'
                    box_index = (i // 3) * 3 + (j // 3) # Calculate the index of the corresponding 3x3 box
                    if (num in rows[i]) or (num in cols[j]) or (num in boxes[box_index]): # Check if the number is already present in the current row, column, or box
                        return False # If it is, the Sudoku board is invalid
                    rows[i].add(num) # Add the number to the current row set
                    cols[j].add(num) # Add the number to the current column set
                    boxes[box_index].add(num) # Add the number to the corresponding box set

        return True # If no duplicates are found, the Sudoku board is valid
        