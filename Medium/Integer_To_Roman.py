# Both solutions achieve optimal O(1) time and space complexity, since the range of
# valid Roman numerals is fixed and bounded (1–3999).
#
# The "OptimizedSolution" version includes practical Python micro-optimizations while
# keeping the code clean and readable:
#
# - Uses a list of (value, symbol) tuples instead of a dictionary:
#   Sequential list iteration avoids hashing overhead and benefits from contiguous
#   memory layout. Since the data is ordered and static, a list is the better choice.
#
# - Uses divmod() to calculate both the quotient and remainder in a single efficient
#   C-level operation, reducing the number of arithmetic operations.
#
# - Builds the output using a list + ''.join() instead of repeated string
#   concatenation, avoiding the creation of many intermediate string objects.
#
# Additional micro-optimizations (e.g., storing method references in local variables)
# can further improve constant-factor speed, but would reduce readability. OptimizedSolution intentionally
# prioritizes clarity while still demonstrating awareness of Python-specific
# performance techniques appropriate for production-quality Python.



class IntuitiveSolution:
    def intToRoman(self, num: int) -> str:
        value_map = {
            1000:"M", 900:"CM", 500:"D", 400:"CD",
            100:"C", 90:"XC", 50:"L", 40:"XL",
            10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"
        }
        roman = ""
        for value, symbol in value_map.items():
            if num == 0:
                return roman
            count = num // value
            num -= count * value
            roman += symbol * count
        return roman
            
            
class OptimizedSolution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        roman = []
        for value, symbol in values:
            if num == 0:
                break
            count, num = divmod(num, value)
            roman.append(symbol * count)
        return "".join(roman)
