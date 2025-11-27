from typing import List
from functools import lru_cache

class OptimalSolution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[i][j][r] = number of ways to reach (i, j) with sum % k == r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]

        start_mod = grid[0][0] % k
        dp[0][0][start_mod] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue  # already initialized

                val_mod = grid[i][j] % k

                for r in range(k):
                    ways = 0
                    if i > 0:
                        ways += dp[i-1][j][r]
                    if j > 0:
                        ways += dp[i][j-1][r]

                    if ways:
                        new_r = (r + val_mod) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + ways) % MOD

        return dp[m-1][n-1][0]



class IntuitedSolution:
    '''
    This solution fails on leetcode due to the recursion depth being limited to 50k, and the test cases will push the solution passed those bounds.
    This solution is however optimal in complexity, running in O(N x M x K) time and using O(M x N x K) space. The problem is that stack space complexity is O(N + M),
    which can exceed the limit in python.

    Therefore this solution runs with optimal time and space complexity but is only applicable for input where N + M < recursion limit.
    '''
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        OUTPUT_MOD = (10**9 + 7)
        row_bound, col_bound = len(grid)-1, len(grid[0])-1

        @lru_cache(None)
        def dfs(i, j, mod_sum):
            # Add current cell value to mod_sum
            mod_sum = (mod_sum + grid[i][j]) % k
            # Base case: reached bottom-right cell
            if i == row_bound and j == col_bound:
                return 1 if mod_sum == 0 else 0
            count = 0
            # Move down
            if i < row_bound:
                count += dfs(i + 1, j, mod_sum)
            # Move right
            if j < col_bound:
                count += dfs(i, j + 1, mod_sum)
            return count % OUTPUT_MOD

        return dfs(0, 0, 0)
    

class Testing:

    # List of test cases: (grid, k, expected_result)
    test_cases = [
        # Provided examples
        ([[5,2,4],[3,0,5],[0,7,2]], 3, 2),
        ([[0,0]], 5, 1),
        ([[7,3,4,9],[2,3,6,2],[2,3,7,0]], 1, 10),

        # Single row
        ([[1,2,3,4,5]], 3, 1),

        # Single column
        ([[2],[4],[6],[1]], 5, 0),

        # No valid paths
        ([[1,1],[1,1]], 5, 0),

    ]

    def assert_solved(expected, actual, grid, k):
        try:
            assert expected == actual, f"Expected result: {expected}\nActual Result: {actual}\nGrid: {grid}\nK = {k}"
        except AssertionError as err:
            print(f"\nSolution Failed\n\t=====\n{err}")

    if __name__ == "__main__":
        solver = OptimalSolution()

        # Run all test cases using optimal solution
        for grid, k, expected in test_cases:
            result = solver.numberOfPaths(grid, k)
            assert_solved(expected, result, grid, k)

        solver = IntuitedSolution()

        # Run all test cases using optimal solution
        for grid, k, expected in test_cases:
            result = solver.numberOfPaths(grid, k)
            assert_solved(expected, result, grid, k)