from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row = any(x for x in matrix if x == 0)
        first_col = any(x for x in matrix[0] if x == 0)

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row:
            matrix[0] = [0] * len(matrix[0])

        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] == 0


class Testing:
    if __name__ == "__main__":
        solver = Solution()
        test_matrix = [
            [1,1,1],
            [1,0,1],
            [1,1,1]
        ]
        expected = [
            [1,0,1],
            [0,0,0],
            [1,0,1]
        ]
        solver.setZeroes(test_matrix)
        if test_matrix == expected:
            print("badabingbadaboom, wadiyatalkinabeet") # Success
        else:
            print("AHHHHHHHHHHHHHH") # Oh No...
            print(test_matrix)