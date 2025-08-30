# https://leetcode.com/problems/valid-sudoku/

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for r in range(9):
            seen_in_row = set()
            for c in range(9):
                num = board[r][c]
                if num != "." and num in seen_in_row:
                    return False  # Repetitive number found in row
                seen_in_row.add(num)

        # Check columns
        for c in range(9):
            seen_in_col = set()
            for r in range(9):
                num = board[r][c]
                if num != "." and num in seen_in_col:
                    return False  # Repetitive number found in column
                seen_in_col.add(num)

        # Check boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen_in_box = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        num = board[r][c]
                        if num != "." and num in seen_in_box:
                            return False
                        seen_in_box.add(num)

        return True


# refactored:
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def _has_duplicate(values: List[str]) -> bool:
            seen = set()
            for val in values:
                if val != ".":
                    if val in seen:
                        return True
                    seen.add(val)
            return False

        # Check rows and columns
        for i in range(9):
            row = board[i]
            col = [board[r][i] for r in range(9)]
            if _has_duplicate(row) or _has_duplicate(col):
                return False

        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = [
                    board[r][c]
                    for r in range(box_row, box_row + 3)
                    for c in range(box_col, box_col + 3)
                ]
                if _has_duplicate(box):
                    return False

        return True
