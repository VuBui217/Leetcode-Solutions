Link to problem: https://leetcode.com/problems/valid-sudoku/description/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Algorithm :
        # Using hashsets to store all the rows , columns, and and sub-
        # boxes of the board
        # If there's any digits that we can't add to one of the hashmaps
        # Return false
        # otherwise return true

        # Create hashsets for rows, cols, and sub_boxes
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)

        # Iterate the board
        for r in range(9):
            for c in range(9):
                # If current element is not a digit, go next
                if board[r][c] == '.':
                    continue
                # Check for valid digit, if current element already
                # exists in one of the hashset
                # Return False
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in sub_boxes[(r//3,c//3)]):
                    return False
                # If current digit doesn't exist, add to corresponding set
                rows[r].add(board[r][c]);
                cols[c].add(board[r][c]);
                sub_boxes[(r//3,c//3)].add(board[r][c])
        # Otherwise return True
        return True
