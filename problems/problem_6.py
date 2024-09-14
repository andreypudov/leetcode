# 6. Zigzag Conversion
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given
# a number of rows:
#
# string convert(string s, int numRows);
#
# Constraints:
#
# - 1 <= s.length <= 1000
# - s consists of English letters (lower-case and upper-case), ',' and '.'.
# - 1 <= numRows <= 1000


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        accumulator = [[] for _ in range(numRows)]

        for index, char in enumerate(s):
            row = index % (2 * numRows - 2)
            if row >= numRows:
                row = 2 * numRows - 2 - row
            accumulator[row].append(char)

        return "".join(["".join(row) for row in accumulator])
