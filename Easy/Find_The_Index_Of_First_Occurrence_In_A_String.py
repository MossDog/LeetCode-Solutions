from typing import List


class OptimalSolution:
    '''
    This is an efficient implementation of the substring search problem using the KMP algorithm.
    It preprocesses the needle to create an LPS (Longest Prefix Suffix) array, which allows the algorithm
    to skip unnecessary comparisons during the search in the haystack.
    This approach has a time complexity of O(n + m), where n is the length of the haystack
    and m is the length of the needle, making it suitable for larger inputs.
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0  # empty needle matches at index 0
        
        # Step 1: Build LPS (Longest Prefix Suffix) array for needle
        lps = self.build_lps(needle)

        # Step 2: Scan haystack using needle and LPS
        hay_index = 0      # index in haystack
        needle_index = 0   # index in needle

        while hay_index < len(haystack):
            if haystack[hay_index] == needle[needle_index]:
                # Characters match, move both pointers
                hay_index += 1
                needle_index += 1

                if needle_index == len(needle):
                    # Full match found
                    return hay_index - needle_index
            else:
                if needle_index != 0:
                    # Mismatch after some matches → jump in needle using LPS
                    needle_index = lps[needle_index - 1]
                else:
                    # Mismatch at start → move haystack pointer forward
                    hay_index += 1

        # No match found
        return -1

    def build_lps(self, pattern: str) -> List[int]:
        """
        Builds the LPS array for KMP.
        LPS[i] = length of longest proper prefix which is also a suffix for pattern[0..i]
        """
        lps = [0] * len(pattern)
        length = 0  # length of previous longest prefix-suffix
        i = 1       # start from second character

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # Mismatch after some matches → jump length using previous LPS
                    length = lps[length - 1]
                else:
                    # No match → LPS is 0
                    lps[i] = 0
                    i += 1

        return lps


class IntuitiveSolution:
    '''
    This is a straightforward implementation of the substring search problem.
    It uses a brute-force approach by checking every possible starting position in the haystack.
    For each starting position, it compares characters one by one with the needle.
    While simple and easy to understand, this approach has a time complexity of O(n*m),
    where n is the length of the haystack and m is the length of the needle.
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1

        h_len = len(haystack)
        n_len = len(needle)

        for i in range(h_len - n_len + 1):
            match = True
            for j in range(n_len):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i

        return -1


class Testing:

    # List of test cases: (haystack, needle, expected_result)
    test_cases = [
        # Repeated characters
        ("ababbababab", "baba", 1),
        ("aaaaaa", "aaa", 0),
        ("aaaaa", "aa", 0),

        # Basic cases
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("abc", "abc", 0),
        ("abc", "d", -1),

        # Needle at start / middle / end
        ("startmiddleend", "start", 0),
        ("startmiddleend", "middle", 5),
        ("startmiddleend", "end", 11),

        # Needle longer than haystack
        ("abc", "abcdef", -1),
        ("", "a", -1),

        # Empty strings
        ("", "", 0),
        ("abc", "", 0),
        ("", "a", -1),

        # Overlapping occurrences
        ("mississippi", "issi", 1),
        ("ababa", "aba", 0),

        # Stress / long inputs
        ("a" * 200, "a" * 100, 0),
        ("a" * 199 + "b", "a" * 200, -1),

        # Edge cases for pointer movement
        ("aaaaab", "aaab", 2),
        ("abcabcabcabc", "cab", 2),
        ("xyz", "yz", 1),
    ]

    def assertSolved(expected, actual):
        try:
            assert expected == actual, f"Expected result: {expected}\nActual Result: {actual}"
        except AssertionError as err:
            print(f"\nSolution Failed\n\t=====\n{err}")

    if __name__ == "__main__":
        solver = OptimalSolution()

        # Run all test cases using optimal solution
        for haystack, needle, expected in test_cases:
            result = solver.strStr(haystack, needle)
            assertSolved(expected, result)

        
        solver = IntuitiveSolution()
        # Run all test cases using intuitive solution
        for haystack, needle, expected in test_cases:
            result = solver.strStr(haystack, needle)
            assertSolved(expected, result)

