# sort colors
# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        row = 0
        column = len(matrix[0]) - 1

        while(row < len(matrix) and column > -1):
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                column -= 1
            elif matrix[row][column] < target:
                row += 1
        return False