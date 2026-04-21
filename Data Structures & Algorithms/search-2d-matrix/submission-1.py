class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        topRow, botRow = 0, rows - 1
        while topRow <= botRow:
            midRow = topRow + ((botRow - topRow) // 2)
            if target > matrix[midRow][-1]:
                topRow = midRow + 1
            elif target < matrix[midRow][0]:
                botRow = midRow - 1
            else:
                break
        if topRow > botRow:
            return False
        midRow = topRow + ((botRow - topRow) // 2)
        l, r = 0, cols - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target > matrix[midRow][m]:
                l = m + 1
            elif target < matrix[midRow][m]:
                r = m - 1
            else:
                return True
        return False