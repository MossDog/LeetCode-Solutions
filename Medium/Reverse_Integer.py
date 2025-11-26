
INT_32_MAX = 2147483647 #(2**31 - 1) 31 because 1 bit is used to store sign of value, -1 to account for 0

class Solution:

    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        x_reversed = 0
        while x != 0:
            digit = x % 10
            x //= 10
            if x_reversed > INT_32_MAX // 10 or (x_reversed == INT_32_MAX // 10 and digit > 7):
                return 0
            
            x_reversed = x_reversed * 10 + digit
            
        return x_reversed * sign



class Testing:

    # List of test cases: (input, expected_result)
    test_cases = [
        (0, 0),
        (5, 5),
        (9, 9),
        (10, 1),
        (120, 21),
        (1000, 1),
        (123, 321),
        (-123, -321),
        (-10, -1),
        (-120, -21),

        (1534236469, 0),
        (-1534236469, 0),
        (2147483647, 0),
        (-2147483648, 0),
        (1463847412, 2147483641),
        (-1463847412, -2147483641),
        (1563847412, 0),

        (1000000003, 0),
        (-1000000003, 0),
        (2147483412, 2143847412),
    ]

    def assertSolved(expected, actual):
        try:
            assert expected == actual, f"Expected result: {expected}\nActual Result: {actual}"
        except AssertionError as err:
            print(f"\nSolution Failed\n\t=====\n{err}")

    if __name__ == "__main__":
        solver = Solution()

        # Run all test cases using intuitive solution
        for input, expected in test_cases:
            result = solver.reverse(input)
            assertSolved(expected, result)

