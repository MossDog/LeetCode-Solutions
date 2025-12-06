from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix[0]), len(matrix)

        first_row = any(matrix[0][j] == 0 for j in range(n))
        first_col = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row:
            matrix[0][:] = [0] * n

        if first_col:
            for i in range(m):
                matrix[i][0] = 0


class Testing:
    if __name__ == "__main__":
        solver = Solution()
        test_matrix = [[0,1,2,0],
                       [3,4,5,2],
                       [1,3,1,5]]
        expected = [[0,0,0,0],
                    [0,4,5,0],
                    [0,3,1,0]]
        solver.setZeroes(test_matrix)
        if test_matrix == expected:
            print("badabingbadaboom, wadiyatalkinabeet") # Success
        else:
            print("AHHHHHHHHHHHHHH") # Oh No...
            print(test_matrix)