Link to the problem: https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Algorithm: Apply Binary Search to rows, and then cols to find the target
        # Time Complexity: O(m*n)
        # Space Complexity: O(1)
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            if (target > matrix[mid_row][-1]):
                top = mid_row + 1
            elif (target < matrix[mid_row][0]):
                bot = mid_row - 1
            else:
                break
        
        row = (top + bot) // 2
        l = 0
        r = cols -1
        while l <= r:
            mid = (l + r) // 2
            if (target == matrix[row][mid]):
                return True
            elif (target > matrix[row][mid]):
                l = mid + 1
            else:
                r = mid - 1
        return False
